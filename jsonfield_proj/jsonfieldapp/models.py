from django.db import models

# Create your models here.
class Example(models.Model):

    data = models.JSONField()