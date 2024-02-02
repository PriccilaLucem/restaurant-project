from flask import request, jsonify, current_app
from app.models.address_model import Address
from app.services.address_services import get_address_zip_code
from app.controllers import is_logged
from app.models.client_model import Client
from jwt.exceptions import InvalidSignatureError
from app.exc.AddressAlreadyRegisteredError import AddressAlreadyRegisteredError

def post_address_controller():
    data = request.json
    try:    
        client_from_token = is_logged(request)
        client = Client.query.get(client_from_token['id'])

        validated_data = Address.validate_args(**data)
        address = get_address_zip_code(validated_data['zip_code'])
        
        verify_if_address_exists = Address.query.filter_by(
            street= address['logradouro'],
            city= address['localidade'],
            state= address['uf'],
            zip_code= address['cep'],
            number= validated_data['number'],
            complement= validated_data['complement'],
        ).first()

        if not verify_if_address_exists:
            address = Address(street= address['logradouro'],
            city= address['localidade'],
            state= address['uf'],
            zip_code= address['cep'],
            number= validated_data['number'],
            complement= validated_data['complement'])
            current_app.db.session.add(address)
            current_app.db.session.commit()
            client.addresses.append(address)
            current_app.db.session.commit()
            
            return jsonify(client)
        
        address = Address(street= address['logradouro'],
        city= address['localidade'],
        state= address['uf'],
        zip_code= address['cep'],
        number= validated_data['number'],
        complement= validated_data['complement'])
        Client.validate_if_user_already_registered_address(client, address)
        current_app.db.session.add(address)
        current_app.db.session.commit()
        client.addresses.append(address)
        current_app.db.session.commit()

        return jsonify(client)
    except KeyError:
        return jsonify({"error": "Token missing"}),401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}),401
    except ValueError:
        return jsonify({"error": "Invalid cep"}),400
    except TypeError as e:
        return jsonify({"error": "Invalid data"}),400
    except AddressAlreadyRegisteredError:
        return jsonify({"error": "Address already registered"}), 400
    

def delete_address_from_client_controller(address_id):
    try:
        client_from_token = is_logged(request) 
        client = Client.query.get(client_from_token['id'])
        address = Address.query.get(address_id)

        if address in client.addresses:
            client.addresses.remove(address)
            current_app.db.session.commit()
            
            return '', 204
        else:
            return jsonify({"error": "Address not associated with the client"}), 404

    except KeyError:
        return jsonify({"error": "Token missing"}), 401
    except InvalidSignatureError:
        return jsonify({"error": "Invalid Token"}), 401