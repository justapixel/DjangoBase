import time
import jwt


def metabase_generate_token(resource_type, value):
    payload = {
        "resource": {f"{resource_type}": value},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }
    token = jwt.encode(
        payload, "25f5798301232936a71cf67387adb92ac4a25684f5705d3d4053af3ba557f14b", algorithm="HS256")

    return token
