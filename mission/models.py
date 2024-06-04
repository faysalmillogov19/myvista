from django.db import models
from vehicule.models import Vehicule
from employe.models import Employe

# Create your models here.

class Mission(models.Model):
    debut=models.DateField()
    fin=models.DateField(null=True)
    depart=models.CharField(max_length=100, null=True)
    destination=models.CharField(max_length=100, null=True)
    vehicule=models.ForeignKey(Vehicule, null=True, on_delete=models.CASCADE)

class Escale(models.Model):
    destination=models.CharField(max_length=100)
    date=models.DateField(null=True)
    mission=models.ForeignKey(Mission, null=True, on_delete=models.CASCADE)

class Membre(models.Model):
    employe=models.ForeignKey(Employe, null=True, on_delete=models.CASCADE)
    mission=models.ForeignKey(Mission, null=True, on_delete=models.CASCADE)