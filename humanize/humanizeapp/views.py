from django.shortcuts import render
import datetime

# Create your views here.
def index(request):

    now = datetime.datetime.now()
    context = {
        'first':6,
        'second':34656353428826577,
        'third':3542,
        'fourth':4512,
        'fifth':12,
        'now':now ,
        'otherdates':now - datetime.timedelta(days=1),
        'tomorrow':now + datetime.timedelta(days=1),
        'future':now + datetime.timedelta(days=542),
        'prevdays':now - datetime.timedelta(days=14),

    }

    return render(request,'myapps/index.html',context)