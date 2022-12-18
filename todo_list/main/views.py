from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import Task
from .forms import TodoForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'TODO MAIN', 'task': tasks})

def login(request):
    return render(request, 'main/login.html')

def about(request):
    return render(request, 'main/about.html')

def todo_list(request):
    todo_items = Task.objects.all().order_by('created_at')
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')

    context = {'todo_items': todo_items}
    return render(request, 'main/base.html', context)

def update_todo(request, pk):
    todo_item = Task.objects.get(id=pk)
    form = TodoForm(instance=todo_item)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form_save()
            return redirect('todo_list')

    context = {'form': form}
    return render(request, 'main/update_todo.html', context)