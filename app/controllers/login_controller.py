from flask import jsonify, request
from app.models.client_model import Client
import jwt
from os import environ

def login_controller():
    data = request.json
    
    if 'email' not in data or 'password' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    client = Client.query.filter_by(email=data['email']).first()
    if not client:
        return jsonify({"error": "Not found"}), 404
    
    if not client.check_password(data['password']):
        return jsonify({"error": "Invalid password"}),401
    
    payload = {
        "name": client.name,
        "email": client.email,
        "id": client.id,
        "type": "user"
    }
    token = jwt.encode(payload, environ.get("JWT_KEY"), algorithm='HS256')

    return jsonify({"token":token}), 200