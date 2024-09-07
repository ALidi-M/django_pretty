from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def index(request):
    form = ContactForm()

    context = { 'form':form}
    return render(request,'myapps/index.html',context)
