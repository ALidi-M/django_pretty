from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
    

class Section(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self) -> str:
        return self.title
    

class Lecture(models.Model):
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.IntegerField()
    code_link = models.CharField(max_length=100,blank=True)
    slug = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


