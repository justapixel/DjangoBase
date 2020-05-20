import time
from django.shortcuts import render
import jwt

METABASE_SITE_URL = "http://localhost:3001"
METABASE_SECRET_KEY = "25f5798301232936a71cf67387adb92ac4a25684f5705d3d4053af3ba557f14b"


def indexboards(request):
    payload_peoples = {
        "resource": {"dashboard": 1},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }

    payload_reviews = {
        "resource": {"dashboard": 3},
        "params": {},
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }

    token = jwt.encode(payload_peoples, METABASE_SECRET_KEY, algorithm="HS256")

    dashboard_peoples = METABASE_SITE_URL + "/embed/dashboard/" + \
        token.decode("utf8") + "#theme=night&bordered=false&titled=true"

    token = jwt.encode(payload_reviews, METABASE_SECRET_KEY, algorithm="HS256")

    dashboard_reviews = METABASE_SITE_URL + "/embed/dashboard/" + \
        token.decode("utf8") + "#theme=night&bordered=false&titled=true"

    return render(request, 'dashboards/index.html', {'dashboard_peoples': dashboard_peoples,
                                                     'dashboard_reviews': dashboard_reviews})


def indexquestions(request):
    payload = {
        "resource": {"question": 5},
        "params": {

        },
        "exp": round(time.time()) + (60 * 10)  # 10 minute expiration
    }

    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    iframe_url = METABASE_SITE_URL + "/embed/question/" + \
        token.decode("utf8") + "#theme=night&bordered=false&titled=true"

    return render(request, 'dashboards/index.html', {'iframe_url': iframe_url})
