from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('<int:programmer_id>/', views.index, name='index'),
]