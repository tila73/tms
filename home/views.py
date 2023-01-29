from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')

def task(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'task/index.html', context)

def addtask(request):
    if request.method == "GET":
        task_form = TaskForm
        return render(request, 'task/add_task.html', context={'form':task_form})
    else:
        task_form = TaskForm(request.POST, request.FILES)
        if task_form.is_valid():
            task_form.save()
            return redirect('task')
    return render(request, 'task/add_task.html', context={'form':task_form})