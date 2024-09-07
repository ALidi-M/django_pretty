from django.shortcuts import render,redirect
from .models import Programmer,Language
from django.forms import modelformset_factory,inlineformset_factory

# Create your views here.

def index(request, programmer_id):
    programmer = Programmer.objects.get(pk=programmer_id)
    LanguageFormset = inlineformset_factory(Programmer, Language, fields=('name',),can_delete=False,extra=1,max_num=3)#pass the 2 models

    if request.method == 'POST':
        formset = LanguageFormset(request.POST, instance=programmer)
        if formset.is_valid():
            formset.save()

            return redirect('index', programmer_id=programmer.id)

    formset = LanguageFormset(instance=programmer)

    return render(request, 'myapps/index.html', {'formset' : formset})

