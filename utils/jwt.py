import jwt
import datetime
from flask import current_app

def generate_token(user_id):
    """
    Generate a JWT token.
    
    Args:
        user_id (int): The user ID.
    
    Returns:
        str: The JWT token.
    """
    payload = {
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1),
        'iat': datetime.datetime.now(datetime.timezone.utc),
        'sub': user_id
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')


def decode_token(token):
    """
    Decode a JWT token.
    
    Args:
        token (str): The JWT token.
    
    Returns:
        int: The user ID if the token is valid, None otherwise.
    """
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

