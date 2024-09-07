from django.contrib import admin
from .models import Language,Framework,Movie,Character
# Register your models here.

admin.site.register(Language)
admin.register(Framework)
admin.register(Movie)
admin.register(Character)
