from django.urls import path

from . import views

urlpatterns = [
    path('painel', views.indexboards, name='indexboards'),
    path('questions', views.indexquestions, name='indexquestions'),
]
