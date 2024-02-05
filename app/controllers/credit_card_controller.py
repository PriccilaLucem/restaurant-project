from flask import jsonify, request, current_app
from app.controllers import is_logged
from app.models.client_model import Client
from app.models.credit_card_model import CreditCard
from jwt.exceptions import InvalidSignatureError


def get_credit_card_controller():
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(decoded_token['id'])
        return jsonify(client.credit_cards)
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401
    
def post_credit_card_controller():
    data = request.json
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(decoded_token['id'])
        
        validated_data = CreditCard.validate_args(**data)
        credit_card = CreditCard(**validated_data)
        credit_card.client_id = client.id
        current_app.db.session.add(credit_card)

        client.credit_cards.append(credit_card)
        current_app.db.session.commit()

        return "",204

    except TypeError:
        return jsonify({"error": "Invalid data"})    
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401

    
def delete_credit_card_controller(credit_card_id):
    try:
        decoded_token = is_logged(request)
        client = Client.query.get(decoded_token['id'])
        for credit_card in client.credit_cards:
            if credit_card.id == credit_card_id:
                card = CreditCard.query.get(credit_card_id)
                current_app.db.session.delete(card)
                current_app.db.session.commit()
                return "",204
        return jsonify({"error": "Card not found"}),404
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401