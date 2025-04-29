from functools import wraps

import jwt
from flask import request

from common.constants import JWT_SECRET_KEY


def token_required():
    def check_token(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            jwt_access_token = request.headers.get('token', None)
            if not jwt_access_token: return {'error': f'TOKEN NOT FOUND'}, 503
            try:
                user = jwt.decode(jwt_access_token, JWT_SECRET_KEY, algorithms='HS256')
                if not (user and user.get('name', None)): raise Exception('')
            except Exception as e:
                return {'error': f'User Unauthorized'}, 503

            result = f(*args, **kwargs)
            return result

        return wrapper

    return check_token