import time
from django.shortcuts import render
import jwt

METABASE_SITE_URL = "http://localhost:3001"
METABASE_SECRET_KEY = "25f5798301232936a71cf67387adb92ac4a25684f5705d3d4053af3ba557f14b"


def indexboards(request):
    payload = {
        "resource": {"dashboard": 1},
        "params": {

        },
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    iframe_url = METABASE_SITE_URL + "/embed/dashboard/" + \
        token.decode("utf8") + "#theme=night&bordered=true&titled=true"

    return render(request, 'dashboards/index.html', {'iframe_url': iframe_url})
