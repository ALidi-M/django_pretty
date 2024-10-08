from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=50)
    population = models.IntegerField()
    country = models.ForeignKey(Country,related_name='cities',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
