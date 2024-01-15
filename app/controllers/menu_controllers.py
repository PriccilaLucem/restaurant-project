from flask import jsonify, request, current_app
from app.models.menu_model import Menu
from app.controllers import is_amd
from jwt.exceptions import InvalidSignatureError

def get_menu_controller():
    return jsonify(Menu.query.all())

def get_by_id_menu_controller(id):
    item = Menu.query.get(id)
    
    if item:
        return jsonify(item)
    return jsonify({"error": "Not found"}), 404

def post_menu_controller():
    if not is_amd(request):
        return {"error": "Unauthorized"},401
    data = request.json

    try:
        Menu.validate_args(**data)
        product = Menu(**data)
        current_app.db.session.add(product)
        current_app.db.session.commit()
        return jsonify(product)

    except TypeError:
        return jsonify({"error": "Invalid data"}), 400
    except ValueError:
        return jsonify({"error": "Invalid data"}), 400
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401


def delete_menu_controller(id):
    try:
        if not is_amd(request):
            return {"error": "Unauthorized"},401
        item = Menu.query.get(id)
        if item:
            current_app.db.session.delete(item)
            current_app.db.session.commit()
            return '',204

        return jsonify({"error": "Not found"}), 404
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401

def patch_menu_controller(id):
    if not is_amd(request):
        return {"error": "Unauthorized"},401
    data = request.json
    valid_args = Menu.check_args(**data)
    try:
        Menu.validate_args(**valid_args)
        Menu.query.filter_by(id=id).update(valid_args)
        current_app.db.session.commit()
        item= Menu.query.get(id)

        if not item:
            return jsonify({"error": "Not Found"}),404 
        return jsonify(item)
    
    except TypeError:
        return jsonify({"error": "Invalid data"}), 400
    except ValueError:
        return jsonify({"error": "Invalid data"}), 400
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401