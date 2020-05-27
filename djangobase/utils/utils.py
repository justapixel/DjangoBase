import time
import jwt
from environ import Env

env = Env()


def metabase_generate_token(resource_type, value, **kwargs):
    params = kwargs.get('params', {})
    exp_time = kwargs.get('exp_time', 10)
    payload = {
        "resource": {f"{resource_type}": value},
        "params": params,
        "exp": round(time.time()) + (60 * exp_time)  # 10 minute expiration
    }
    metabase_key = env('METABASE_SECRET_KEY')
    token = jwt.encode(
        payload, metabase_key, algorithm="HS256")

    return token
