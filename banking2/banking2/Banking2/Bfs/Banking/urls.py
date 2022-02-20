from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.homepage, name='Banking-homepage'),
    path('login/', views.login, name='Banking-login'),
    path('register/', views.register, name='Banking-register'),
    path('addRegister/', views.addRegister, name='addRegister'),
    path('checklogin', views.checklogin, name='checklogin'),
]