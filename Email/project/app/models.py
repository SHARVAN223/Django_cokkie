from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length = 50)
    Email = models.EmailField()
    City = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
