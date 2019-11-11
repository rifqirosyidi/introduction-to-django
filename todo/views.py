from django.shortcuts import render
from .models import Todo


# Create your views here.
def index(request):
    list_todo = Todo.objects.order_by('id')
    context = {'list_todo': list_todo}
    return render(request, 'todo/index.html', context)