import jwt
import os

def is_amd(request):
    token = request.headers['Authorization'].split(" ")[1]
    decoded_token = jwt.decode(token, os.environ.get("JWT_KEY"), algorithms=['HS256'])
    if decoded_token.user is "adm":
        return True
    return False

def is_logged(request):
    token = request.headers['Authorization'].split(" ")[1]
    decoded_token = jwt.decode(token, os.environ.get("JWT_KEY"), algorithms=['HS256'])
    return decoded_token