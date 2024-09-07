from django.db import models
import requests

# Create your models here.
class Location(models.Model):
    zip_code = models.IntegerField()
    latitude = models.DecimalField(blank=True,max_digits=9,decimal_places=6)
    longitude = models.DecimalField(blank=True,max_digits=9,decimal_places=6) 


    def save(self,*args,**kwargs):

        r = requests.get(f'https://example.com/api/explore/v2.1/catalog/datasets/georef-united-states-of-america-zc-point@public/records?select={self.zip_code}&limit=20')
        self.latitude = r.json()['records'][0]['fields']['latitude']
        self.longitude = r.json()['records'][0]['fields']['longitude']
        self.latitude = 123.456
        self.longitude = 123.456

        super().save(*args,**kwargs)


    def __str__(self):
        return str(self.zip_code)