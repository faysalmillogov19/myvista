from django.shortcuts import render, redirect
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin
from django.forms.models import model_to_dict
import datetime

from vehicule.models import Vehicule, Marque, Categorie, Carburant, Type as Type_vehicule
from panne.models import Panne, Devis, Type
from consommation.models import Consommation
from entretien.models import Entretien, Type_entretien
from django.contrib.auth.models import User,Group
from django.db.models import Q, Avg, Sum, Max,Count

import matplotlib.pyplot as plt
import pandas as pd
import os
import shutil
import numpy as np


#data=model_to_dict(query, fields=('id', 'vehicule_id', 'type_id', 'pieces', 'description', 'date','immobile'))

@is_admin
def index(request):
    total_vehicule=Vehicule.objects.all().count()
    cammember_vehicule=stat_all_vehicule()
    graphic_consommation=stat_all_consonsommation()
    return render(request,'index.html',
        {
            "total_vehicule":total_vehicule,
            "cammember_vehicule":cammember_vehicule, "graphic_consommation":graphic_consommation,
        }
    )

def stat_all_vehicule():
    
    try:

        x=[Vehicule.objects.filter(desactivate=False).count(), Vehicule.objects.filter(desactivate=True).count()]
        y=["Actif", "Desactive"]
        
        plt.figure()
        plt.pie(x, labels=y, autopct="%1.1f%%")

        file_name='graphic.png'
        plt.title("Etat des vehicules")
        plt.legend(prop = {'size': 12})
        plt.savefig(file_name)
        file_url='stats/'+'cammembert_all_vehicule_.png'
        shutil.move(file_name, "static/"+file_url)
        return file_url
    except:
        return False
    
def stat_all_consonsommation():
    query=Consommation.objects.all().order_by('date').values()
    data=[]
    try:
        for row in query:
            k=[row["date"].strftime("%d/%m/%Y"), row["montant"]]
            data.append(k)
        
        df=pd.DataFrame(data, columns=['date','montant'])
        plt.figure()
        df.groupby('date').sum().plot(kind='line') #.groupby('structure').count()
        file_name='graphic.png'
        plt.title("Graphique de consommation")
        plt.savefig(file_name)
        file_url='stats/'+'graphic_all_consommation.png'
        shutil.move(file_name, "static/"+file_url)
        return file_url
    except:
        return False