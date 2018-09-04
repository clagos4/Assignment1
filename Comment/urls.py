from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list_comments/', views.list_comments)
]