from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_view, name="list"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete"),
]
