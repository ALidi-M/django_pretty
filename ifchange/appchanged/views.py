from django.shortcuts import render

# Create your views here.

def index(request):

    dict_values = [
        {'name':'Ahmad','language':'Python'},
        {'name':'Ahmad','language':'Ruby'},
        {'name':'Ashley','language':'Javascript'},
        {'name':'Ashley','language':'Python'},
        {'name':'Brian','language':'C++'}

    ]
    values = ['Python','Python','Python','Ruby','Java','Java','JavaScript','JavaScript']
    context = {'values':dict_values}

    return render(request,'myapps/index.html',context)
