from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_default'),
    path('home/', views.home, name='home'),
    path('student/', views.student_form, name='student_form'),
    path('student_data/', views.student_data, name='student_data'),
    path('show_students/', views.show_students, name='show_students'),
]