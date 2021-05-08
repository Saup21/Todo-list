from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('register/', views.register_request, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', views.logout_request, name='logout'),
]
