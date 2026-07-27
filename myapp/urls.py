from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    path('home/', views.home, name='home'),
    path('empform/', views.empform, name='empform'),
    path('empdata/', views.empdata, name='empdata'),
    path('crud/', views.crud, name='crud_dashboard'),
    path('crud_data/', views.crud_data, name='crud_data'),
    path('update/', views.update, name='update'),
    path('product/', views.product, name='product'),
    path('product_data/', views.product_data, name='product_data'),
    path('show_product/', views.show_product, name='show_product'),
    path('delete',views.delete,name='delete'),
    path('edit',views.edit,name='edit'),
    path('signupform/',views.signupform,name='signupform'),
    path('signupdata/',views.signupdata,name='signupdata'),
    path('loginform/',views.loginform,name='loginform'),
    path('logindata/',views.logindata,name='logindata'),
    path('userlogout/',views.userlogout,name='userlogout')
]
