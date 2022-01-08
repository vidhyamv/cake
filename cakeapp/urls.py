from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('order/',views.order,name='order'),
    path('cake/',views.allprodcat,name='cake'),
]
