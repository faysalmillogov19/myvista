from django.db import models
from vehicule.models import Vehicule

# Create your models here.
class Type_entretien(models.Model):
    libelle=models.TextField()
    duree_moyenne=models.FloatField(null=True)


class Entretien(models.Model):
    description=models.TextField(null=True)
    date=models.DateField()
    nombre=models.FloatField(null=True)
    montant=models.FloatField(null=True)
    type=models.ForeignKey(Type_entretien, null=True, on_delete=models.CASCADE)
    vehicule=models.ForeignKey(Vehicule, null=True, on_delete=models.CASCADE)