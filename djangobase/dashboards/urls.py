from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexpage, name='indexpage'),
    path('panels', views.indexpanels, name='indexpanels'),
    path('questions', views.indexquestions, name='indexquestions'),
]
