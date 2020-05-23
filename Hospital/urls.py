from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('register/',views.Register,name='register'),
    path('login/',views.UserLogin,name='login'),
    ]