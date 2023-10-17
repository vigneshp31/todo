from django.shortcuts import render, redirect, get_object_or_404
from todoapp.models import *
from django.http import HttpResponse

# Create your views here.

def addTask(request):
    if(request.method == 'POST'):
        task = request.POST['task']
        new_task = Task.objects.create(task = task)
        new_task.save()
        return redirect('home')
    return render(request, 'home.html')

def mark_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    print(task)
    task.is_completed = True
    task.save()
    return redirect('home')

def undo(request, pk):
    undo_task = get_object_or_404(Task, pk=pk)
    undo_task.is_completed=False
    undo_task.save()
    return redirect('home')

def edit(request, pk):
    edit_task = get_object_or_404(Task, pk=pk)
    if(request.method=='POST'):
        updated_task = request.POST['updated_task']
        edit_task.task = updated_task
        edit_task.save()
        return redirect('home')
    else:
        return render(request, 'edit.html', context={'edit_task': edit_task})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')