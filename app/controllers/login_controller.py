from flask import jsonify, request
from app.models.client_model import Client
from  app.models.adm_model import Adm
import jwt
from os import environ
def login_controller():

    data = request.json
    
    if 'email' not in data or 'password' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    adm = Adm.query.filter_by(email=data['email']).first()
    client = Client.query.filter_by(email=data['email']).first()

    if not adm:
        if not client:
            return jsonify({"error": "Not found"}), 404
    
        if not client.check_password(data['password']):
            return jsonify({"error": "Invalid password"}),401
    
    payload = {
        "name": client.name if client else adm.name,
        "email": client.email if client else adm.email,
        "id":  client.id if client else adm.id,
        "type": "user" if client else "adm"
    }
    token = jwt.encode(payload, environ.get("JWT_KEY"), algorithm='HS256')

    return jsonify({"token":token}), 200