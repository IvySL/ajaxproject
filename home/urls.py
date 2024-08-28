from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]

urlpatterns = [
    path('/json', views.json_demo),
]