from django.db import models

# Create your models here.
class Simple(models.Model):
    text = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.text