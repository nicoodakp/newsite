# sendemail/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.emailView, name='email'),
    path('success/', views.successView, name='success'),]
