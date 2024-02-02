from flask import request, jsonify, current_app
from app.controllers import is_logged
from app.models.client_model import Client
from app.models.cart_model import Cart
from app.models.menu_model import Menu
from app.models.cart_menu_model import Cart_Menu
from jwt.exceptions import InvalidSignatureError
import ipdb

def get_cart_controller():
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(decoded_token['id'])

        return jsonify(client.cart)
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401
    
def post_cart_controller():
    data = request.json
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(decoded_token['id'])
        
        Cart.valid_args(**data)

        product = Menu.query.get(data['id'])
        cart_menu = Cart_Menu(cart_id=client.cart.id,menu_id=product.id)
        
        for cart_menu in client.cart.cart_relationship:
            if cart_menu.menu_id == product.id:
                return jsonify({"error": "Item already in cart"}), 400
        product.cart_relationship.append(cart_menu)
        current_app.db.session.commit()

        return client.cart.cart_relationship
    except IndexError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401
    except TypeError:
        return jsonify({"error": "Invalid id"}),400
    except AttributeError:
        return jsonify({"error": "Invalid id"}),400
    
    
def patch_cart_controller(product_id):
    data = request.json
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(decoded_token['id'])

        for cart_menu in client.cart.cart_relationship:
            if cart_menu.menu_id == product_id:
                Cart_Menu.validate_args(**data)
                for key, value in data.items():
                    setattr(cart_menu, key, value)
                current_app.db.session.commit()
                return jsonify(client.cart),200
    
        return {"error": "Product is not on cart"},400

    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401
    except TypeError:
        return jsonify({"error": "Invalid data"}),400


def delete_cart_product_controller(product_id):
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(decoded_token['id'])
        for cart_menu in client.cart.cart_relationship:
            if cart_menu.menu_id == product_id:
                to_delete = Cart_Menu.query.get(cart_menu.id)
                current_app.db.session.delete(to_delete)
                current_app.db.session.commit()
                return '',204
        return jsonify({"error": "Product not found"}),404
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401