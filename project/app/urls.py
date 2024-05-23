from django.urls import path
from .views import *

urlpatterns = [
    path('',Register,name='resgiter'),
    path('registerdata/',RegisterData,name='registerdata'),
    path('login/',login,name='login'),
    path('logindata/',logindata,name='logindata'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',logout,name='logout'),
    
]