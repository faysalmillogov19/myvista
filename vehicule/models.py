from django.db import models
from employe.models import Client
from django.contrib.auth.models import User,Group

# Create your models here.
class Categorie(models.Model):
    libelle=models.CharField(max_length=50)
    description=models.CharField(max_length=50)

class Marque(models.Model):
    libelle=models.CharField(max_length=50)

class Type(models.Model):
    libelle=models.CharField(max_length=50)

class Carburant(models.Model):
    libelle=models.CharField(max_length=50)

class Vehicule(models.Model):
    immatriculation=models.CharField(max_length=250,null=True)
    modele=models.CharField(max_length=250,null=True)
    date=models.DateField(null=True)
    carburant=models.ForeignKey(Carburant, null=True, on_delete=models.CASCADE)
    type=models.ForeignKey(Type, null=True, on_delete=models.CASCADE)
    marque=models.ForeignKey(Marque, null=True, on_delete=models.CASCADE)
    categorie=models.ForeignKey(Categorie, null=True, on_delete=models.CASCADE)
    proprio=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
