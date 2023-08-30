from django.shortcuts import render, redirect, get_object_or_404
from todoApp.models import Task
from django.http import HttpResponse

# Create your views here.


def index(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_task = Task.objects.filter(is_completed=True)
    return render(request, "todoApp/index.html", context={"tasks": tasks, "completed_task": completed_task})

def addtask(request):
    task = request.POST.get("task")
    Task.objects.create(task=task)
    return redirect("index")

def done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect("index")

def undo(request, id):
    task = get_object_or_404(Task, id=id)
    task.is_completed = False
    task.save()
    return redirect("index")

def edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if(request.method=="POST"):
        new_task = request.POST.get("update")
        task.task=new_task
        task.save()
        return redirect("index")
    
    return render(request, "todoApp/edit.html", context = {"task": task})


def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("index")