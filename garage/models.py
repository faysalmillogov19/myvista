from django.db import models

# Create your models here.
class Garage(models.Model):
    denomination=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    bp=models.CharField(max_length=50)
