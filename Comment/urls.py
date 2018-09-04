from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_comments, name="list_comments"),
    path('new', views.create_comment, name="create_comment"),
]