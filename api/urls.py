from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),  #http://127.0.0.1:8000/api
    path('cities/', views.cities), #http://127.0.0.1:8000/api/cities
    #path('disctrict/', views.disctricts)  #http://127.0.0.1:8000/api/districts/?city=金門縣
    path('districts/<str:city_name>', views.districts)#http://127.0.0.1:8000/api/districts/金門縣
]  