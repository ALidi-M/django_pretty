from django.shortcuts import render

# Create your views here.
from .form import ExampleForm, ExampleModelForm

def index(request):
    form = ExampleForm() 
    return render(request, 'myapps/index.html', {'form': form})