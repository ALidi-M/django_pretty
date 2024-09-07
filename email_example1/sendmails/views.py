from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def index(request):

    send_mail(
        'Hello from django mail services','Hello there This is an automated message','ahmadmponda@outlook.com',
        ['topacic667@joeroc.com'],fail_silently=False
    )

    return render(request,'myapps/index.html')