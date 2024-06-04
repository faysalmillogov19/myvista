from django.db import models
from garage.models import Garage
from django.contrib.auth.models import User,Group


# Create your models here.

class Poste(models.Model):
    libelle=models.CharField(max_length=100)

class Employe(models.Model):
    matricule=models.CharField(max_length=20, null=True)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=100, null=True)
    date_naissance=models.DateField(null=True)
    lieu_naissance=models.CharField(max_length=100, null=True)
    poste=models.ForeignKey(Poste, null=True, on_delete=models.CASCADE)

class Client(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    telephone1=models.CharField(max_length=12)
    telephone2=models.CharField(max_length=12, null=True)




