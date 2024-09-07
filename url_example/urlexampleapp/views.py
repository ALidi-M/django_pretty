from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request,username='Default User'):

    return HttpResponse('<h1>Welcome to the profile page {}</h1>'.format(username))

def article(request,article_value):
    return HttpResponse('<h1>This is the article page {}</h1>'.format(article_value))