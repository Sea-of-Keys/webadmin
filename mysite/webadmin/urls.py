from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.users, name="users"),
    path("user/<int:id>", views.user, name="user"),
    path("rooms", views.rooms, name="rooms"),
    path("room/<int:id>", views.room, name="room"),
    path("login", views.login, name="login"),
    
]