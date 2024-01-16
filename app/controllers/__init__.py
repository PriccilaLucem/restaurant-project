import jwt
import os
import ipdb

def is_adm(request):
    token = request.headers['Authorization'].split(" ")[-1]
    decoded_token = jwt.decode(token, os.environ.get("JWT_KEY"), algorithms=['HS256'])
    if decoded_token['type'] is "adm":
        return True
    return False

def is_logged(request):
    token = request.headers['Authorization'].split(" ")[1]
    decoded_token = jwt.decode(token, os.environ.get("JWT_KEY"), algorithms=['HS256'])
    return decoded_token

def can_acess(decoded_token, client):
    if decoded_token['id'] != client.id:
        return False
    return True