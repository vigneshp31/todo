from django.shortcuts import render
from todoapp.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    return render(request, 'home.html', context = {'tasks': tasks, 'completed_tasks': completed_tasks})