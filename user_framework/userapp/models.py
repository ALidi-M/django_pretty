from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    # location = models.CharField(max_length=30)
    # age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)



    def __str__(self) -> str:
        return self.user.username 
    
    