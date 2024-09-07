from django.shortcuts import render
from django.forms import modelformset_factory
from .models import Formset
# Create your views here.

def index(request):

    ExampleFormSet = modelformset_factory(Formset,fields=('name','location'),extra=4)

    if request.method == 'POST':

        form = ExampleFormSet(request.POST) #queryset=Formset.objects.none()
        # instances = form.save(commit=False)

        # for instance in instances:
        #     instance.save()
        instances = form.save()

    form = ExampleFormSet()

    return render(request,'myapps/index.html',{'form':form})
