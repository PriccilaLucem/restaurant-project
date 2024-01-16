from flask import jsonify, current_app, request
from app.models.client_model import Client
from sqlalchemy.exc import IntegrityError
from app.controllers import is_adm, can_acess, is_logged
from jwt.exceptions import InvalidSignatureError

def get_all_clients_controller():
    if is_adm(request):
        return {"error": "Unauthorized"},401
    return jsonify(Client.query.all())


def get_by_id_client_controller(id):
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(id)
        if is_adm or not can_acess(decoded_token, client):
            return {"error": "Unauthorized"},401
        if client:
            return jsonify(client)
        return jsonify({"error": "Not found"}),404
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401

def post_client_controller():
    data = request.json
    
    try:
        valid_data = Client.validate_keys(**data)
        password_to_hash = data.pop('password')
        client = Client(**valid_data)
        client.password = password_to_hash
        current_app.db.session.add(client)
        current_app.db.session.commit()
        return jsonify(client),200
    except IntegrityError as e:
        return {"error": "Email already taken"},409

    except KeyError as e:
        return {
            "error": "Invalid data"},400

    except ValueError as e:
        return {"error": e.args[0]},400
    
def patch_client_controller(id):
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(id)
        if not can_acess(decoded_token, client):
            return {"error": "Unauthorized"},401
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401
    data = request.json
    if 'email' in data:
        data.pop('email')
    if 'address' in data:
        data.pop('address')
    valid_data = Client.validate_keys(**data)
    Client.query.filter_by(id=id).update(valid_data)
    current_app.db.session.commit()
    client = Client.query.get(id)
    return jsonify(client), 202

def delete_client_controller(id):
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(id)
        if is_adm or can_acess(decoded_token, client):
            return {"error": "Unauthorized"},401
        if client:
            current_app.db.session.delete(client)
            current_app.db.session.commit()
            return "", 204
        return jsonify({"error": "Not found"}),404
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401