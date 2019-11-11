from django.shortcuts import render
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
