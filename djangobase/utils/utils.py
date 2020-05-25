import time
import jwt
from environ import Env

env = Env()


def metabase_generate_token(resource_type, value):
    payload = {
        "resource": {f"{resource_type}": value},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }
    token = jwt.encode(
        payload, env('METABASE_SECRET_KEY'), algorithm="HS256")

    return token
