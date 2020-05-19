from django.urls import path

from .views import *

urlpatterns = [
    path('index', indexboards, name='index')
]