from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('getform/', views.getform, name='getform'),
    path('data/', views.data, name='getdata'),
    path('empform/', views.empform, name='empform'),
    path('empdata/', views.empdata, name='empdata'),
    path('crud/', views.crud, name='crud_home'),
    path('crud-data/', views.crud_data, name='crud_data'),
]