from django.contrib import admin
from django.urls import path
from todoApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addtask/', views.addtask, name="addtask"),
    path("done/<int:pk>/", views.done, name="done"),
    path("undo/<int:id>/", views.undo, name="undo"),
    path("edit/<int:pk>/", views.edit, name="edit"),
    path("delete/<int:id>/", views.delete, name="delete"),
]