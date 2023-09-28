from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("users", views.users, name="users"),
    path("rooms", views.users, name="rooms"),
    path("login", views.login, name="login"),
    path("user/<int:id>", views.user, name="user"),
]