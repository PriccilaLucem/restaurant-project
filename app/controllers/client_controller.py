from flask import jsonify, current_app, request
from app.models.client_model import Client
from sqlalchemy.exc import IntegrityError



def get_all_clients_controller():
    return jsonify(Client.query.all())


def get_by_id_client_controller(id):
    client = Client.query.get(id)
    if client:
        return jsonify(client)
    return jsonify({"error": "Not found"}),404


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
    data = request.json
    if 'email' in data:
        data.pop('email')
    if 'address' in data:
        ...
    
    valid_data = Client.validate_keys(**data)
    Client.query.filter_by(id=id).update(valid_data)
    current_app.db.session.commit()
    client = Client.query.get(id)
    return jsonify(client), 202

def delete_client_controller(id):
    client = Client.query.get(id)
    
    if client:
        current_app.db.session.delete(client)
        current_app.db.session.commit()
        return "", 204
    return jsonify({"error": "Not found"}),404
