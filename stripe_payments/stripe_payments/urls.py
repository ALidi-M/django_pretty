# """
# URL configuration for stripe_payments project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from paymentapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.index,name='index'),
#     path('thanks/',views.thanks,name='thanks'),
# ]
from django.contrib import admin
from django.urls import path
from paymentapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('thanks/', views.thanks, name='thanks'),
    path('checkout/', views.create_checkout, name='checkout'), 
    path('stripe_webhook/',views.stripe_webhook,name='stripe_webhook')
]

# stripe listen --forward-to localhost:8000/stripe_webhooks/