from django.contrib import admin

# Register your models here.
from .models import Formset

admin.site.register(Formset)