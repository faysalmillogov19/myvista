from django.db import models
from vehicule.models import Vehicule
from garage.models import Garage

# Create your models here.
class Type(models.Model):
    libelle=models.CharField(max_length=50)

class Panne(models.Model):
    vehicule=models.ForeignKey(Vehicule, null=True, on_delete=models.CASCADE)
    pieces=models.TextField()
    description=models.TextField(null=True)
    date=models.DateField(null=True)
    type=models.ForeignKey(Type, null=True, on_delete=models.CASCADE)
    immobile=models.BooleanField(default=False)


class Devis(models.Model):
    panne=models.ForeignKey(Panne, null=True, on_delete=models.CASCADE)
    garage=models.ForeignKey(Garage, null=True, on_delete=models.CASCADE)
    proforma=models.FileField(upload_to='panne/proforma/', max_length=254, null=True)
    facture=models.FileField(upload_to='panne/facture/', max_length=254, null=True)
    cout_devis=models.FloatField(null=True)
    cout_reparation=models.FloatField(null=True)
    date_devis=models.DateField(null=True)
    date_reparation=models.DateField(null=True)
    accepter=models.BooleanField(default=False)



