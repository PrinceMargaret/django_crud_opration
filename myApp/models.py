from django.db import models
from django.db.models.base import Model

# Create your models here.
class Person(models.Model):
    
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    def __str__(self):
        return self.fname+" "+self.lname