from django.db import models
from vehicule.models import Vehicule

# Create your models here.

class Consommation(models.Model):
    date=models.DateField()
    montant=models.FloatField(null=True)
    vehicule=models.ForeignKey(Vehicule, null=True, on_delete=models.CASCADE)