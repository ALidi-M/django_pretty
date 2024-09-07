from django.shortcuts import render
from .models import Member
from django.http import HttpResponse

# Create /your views here.
def index(request):

    # member_one = Member(name='Anthony',location='Las Vegas')
    # member_one.save()

    member_three = Member.objects.get(pk=1)
    
    # member_two = member_one
    member_three.pk = None
    member_three.id = None
    member_three.name = 'Anthony'
    member_three.location = 'Las Vegas'
    member_three.save()

    member_one = Member.objects.get(pk=1)
    

    context = {'member_one':member_one,
               'member_three':member_three}

    return render(request,'myapps/index.html',context)
