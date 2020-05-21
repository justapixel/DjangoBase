from django.urls import path

from . import views

urlpatterns = [
    path('panel', views.indexpanels, name='indexpanels'),
    path('questions', views.indexquestions, name='indexquestions'),
]
