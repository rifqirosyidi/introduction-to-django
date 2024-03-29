from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    list_todo = Todo.objects.order_by('id')
    form = TodoForm()

    context = {
        'list_todo': list_todo,
        'form': form
    }
    return render(request, 'todo/index.html', context)


@require_POST
def add_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('index')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def delete_complete(request):
    todo = Todo.objects.filter(complete=True)
    todo.delete()

    return redirect('index')


def delete_all(request):
    todo = Todo.objects.all()
    todo.delete()

    return redirect('index')

