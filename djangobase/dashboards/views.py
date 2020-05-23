from django.shortcuts import render
from utils.utils import metabase_generate_token

METABASE_SITE_URL = "http://localhost:3001"


def indexpage(request):
    return render(request, 'indexpage/index.html')


def indexpanels(request):

    dashboard_peoples = METABASE_SITE_URL + "/embed/dashboard/" + \
        metabase_generate_token("dashboard", 1).decode(
            "utf8") + "#theme=night&bordered=false&titled=true"

    dashboard_reviews = METABASE_SITE_URL + "/embed/dashboard/" + \
        metabase_generate_token("dashboard", 3).decode(
            "utf8") + "#theme=night&bordered=false&titled=true"

    return render(request, 'panels/index.html', {'dashboard_peoples': dashboard_peoples,
                                                 'dashboard_reviews': dashboard_reviews})


def indexquestions(request):

    iframe_question_5 = METABASE_SITE_URL + "/embed/question/" + \
        metabase_generate_token("question", 5).decode(
            "utf8") + "#theme=night&bordered=false&titled=true"

    return render(request, 'questions/index.html', {'iframe_question_5': iframe_question_5})
