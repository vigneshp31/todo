from django.urls import path
from todoapp import views

urlpatterns = [
    path('add_task/', views.addTask, name="addTask"),
    path('mark_done/<int:pk>/', views.mark_done, name='mark_done'),
    path('undo/<int:pk>/', views.undo, name="undo"),
    path('edit/<int:pk>', views.edit, name="edit"),
    path('delete_task/<int:pk>', views.delete_task, name="delete_task"),
]