from django.shortcuts import render,redirect
from .models import Entry
from .forms import EntryForm


# Create your views here.

def index(request):

    entries = Entry.objects.order_by('-date') #displays objs in reverse
    context = {'entries': entries}
    return render(request,'myapps/index.html',context)

def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()  #adds/insert data into th database
            return redirect('index')
        
    else:

        form = EntryForm()
        
    context = {'form':form}

    return render(request,'myapps/add.html',context)