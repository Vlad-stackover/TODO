from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'TODO MAIN', 'task': tasks})

def login(request):
    return render(request, 'main/login.html')

def about(request):
    return render(request, 'main/about.html')