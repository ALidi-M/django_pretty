from django.urls import path
from . import views

urlpatterns = [
    path('profile/28/',views.profile),
    path('profile/<int:username>/',views.profile),
    path('profile/',views.profile),
    path('profile/<slug:article_value>/',views.article),

]