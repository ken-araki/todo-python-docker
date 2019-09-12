from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import render
from todo.models import Todo, TodoForm

def index(request):
    return HttpResponseRedirect(reverse('todo:search'))

def search(request):
    list = Todo.objects.all()
    params = { 'list' : list }
    return render(request, 'todo/search.html', params)

def edit(request, todo_id):
    todoForm = TodoForm()
    if todo_id > 0:
        todo = Todo.objects.get(todo_id=todo_id)
        todoForm = TodoForm(instance=todo)

    params = {
        'todo_id' : todo_id,
        'form' : todoForm
    }
    return render(request, 'todo/edit.html', params)

def regist(request):
    todo_id = request.POST.get('todo_id')
    todo = Todo()
    if int(todo_id) > 0:
        todo = Todo.objects.get(todo_id=todo_id)
    todoForm = TodoForm(request.POST, instance=todo)
    if todoForm.is_valid():
        todoForm.save()
        return HttpResponseRedirect(reverse('todo:search'))
    else:
        todo_id = request.POST.get('todo_id')
        params = {
            'todo_id' : todo_id,
            'form' : todoForm,
        }
        return render(request, 'todo/edit.html', params)
