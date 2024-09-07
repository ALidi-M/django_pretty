import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Standalone_example.settings')
django.setup()

from Standaloneapp.models import Person

new_person = Person(name='Britney')
new_person.save()
