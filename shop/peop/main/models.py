from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=16)
    phone = models.CharField(max_length=12)