import jwt
import datetime

def generar_jwt(id, secret_key):
    playload = {
        'usuario_id': id,
        'exp': datetime.datetime.now() + datetime.timedelta(hours=24),
        'iat': datetime.datetime.now()
    } 
    
    return jwt.encode(playload, secret_key, algorithm='HS256')