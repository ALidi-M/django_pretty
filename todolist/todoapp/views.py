from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo
from django.http import HttpResponse
from .forms import TodoForm,NewTodoForm
from django.views.decorators.http import require_POST
import datetime

# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')
    # form = TodoForm()

    newtodoform =  NewTodoForm()
    mydate = datetime.datetime.now()


    context = {'todo_list': todo_list, 'form': newtodoform,'mydate':mydate}

    return render(request,'myapps/index.html',context)


@require_POST
def addTodo(request):

    # todo_10 =Todo.objects.get(pk = 15 ) 
    form = TodoForm(request.POST)
    # newtodoform = NewTodoForm(request.POST, instance=todo_10)

    # if newtodoform.is_valid():
    if form.is_valid():

        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
         new_todo = Todo(text=form.cleaned_data['text'])
         new_todo.save()
        #  new_todo = newtodoform.save()

    return redirect('index')

def completeTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact = True).delete()

    return redirect('index')

def deleteAll(request):

    Todo.objects.all().delete()

    return redirect('index')
