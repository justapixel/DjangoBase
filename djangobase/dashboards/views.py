from environ import Env
from django.shortcuts import render
from utils.utils import metabase_generate_token
import jwt
import time

env = Env()

METABASE_SITE_URL = env('METABASE_SITE_URL')


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

    iframe_question_4 = METABASE_SITE_URL + "/embed/question/" + \
        metabase_generate_token("question", 4).decode(
            "utf8") + "#theme=night&bordered=false&titled=true"

    iframe_question_5 = METABASE_SITE_URL + "/embed/question/" + \
        metabase_generate_token("question", 5).decode(
            "utf8") + "#theme=night&bordered=false&titled=true"

    iframe_question_17 = METABASE_SITE_URL + "/embed/question/" + \
        metabase_generate_token("question", 17).decode(
            "utf8") + "#theme=night&bordered=false&titled=true"

    iframe_question_22 = METABASE_SITE_URL + "/embed/question/" + \
        metabase_generate_token("question", 22).decode(
            "utf8") + "#theme=night&bordered=false&titled=true"

    iframe_question_25 = METABASE_SITE_URL + "/embed/question/" + \
        metabase_generate_token("question", 25).decode(
            "utf8") + "#theme=night&bordered=false&titled=true"

    return render(request, 'questions/index.html', {'iframe_question_4': iframe_question_4,
                                                    'iframe_question_5': iframe_question_5,
                                                    'iframe_question_17': iframe_question_17,
                                                    'iframe_question_22': iframe_question_22,
                                                    'iframe_question_25': iframe_question_25})
