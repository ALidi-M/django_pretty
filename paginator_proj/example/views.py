from django.shortcuts import render
from .models import Stuff
from django.core.paginator import Paginator,EmptyPage

# Create your views here.
def index(request):

    # for num in range(100):
    #     stuff = Stuff(name=f'Stuff{num}')
    #     stuff.save()

    stuff_items = Stuff.objects.all()

    p = Paginator(stuff_items,12)
    page_num = request.GET.get('page',1)
    print('Number of Pages: ')
    print(p.num_pages)
    
    try:
        page = p.page(page_num)

    except EmptyPage:
        page = p.page(1)

    context = {'items':page}

    return render(request,'myapps/index.html',context)