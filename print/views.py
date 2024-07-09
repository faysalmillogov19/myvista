from django.shortcuts import render, redirect
from vehicule.models import Vehicule, Marque, Categorie, Carburant, Type as Type_vehicule
from panne.models import Panne, Devis, Type
from consommation.models import Consommation
from entretien.models import Entretien, Type_entretien
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg, Sum, Max
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin
from django.http import JsonResponse
import folium

import matplotlib.pyplot as plt
import pandas as pd
import os
import shutil
import geopandas
import matplotlib.pyplot as plt
from geodatasets import get_path

from tracking.views import stat_all_consonsommation, stat_all_vehicule
import json

# Create your views here.
def recapitulatif(request):
    marques=Marque.objects.all().order_by('libelle').values()
    categories=Categorie.objects.all()
    carburants=Carburant.objects.all()
    types=Type_vehicule.objects.all()
    count_vehicule=4 #Vehicule.objects.all()
    mean_vehicule=3
    vehicules=Vehicule.objects.all()

    cammember_vehicule=stat_all_vehicule()
    graphic_consommation=stat_all_consonsommation()

    return render(
        request, 'print/recapitulatif.html', 
        {
            'vehicules': vehicules, 'count_vehicule':count_vehicule, 'mean_vehicule':mean_vehicule,
            'marques':marques, "categories":categories, "types":types, "carburants":carburants,
            "cammember_vehicule":cammember_vehicule, "graphic_consommation":graphic_consommation
        }
    )

def vehicule(request, id):
    vehicule=Vehicule.objects.get(id=id)
    vehicules=Vehicule.objects.filter(~Q(id=id))
    pannes=Panne.objects.filter(vehicule_id=id)

    entretiens=Entretien.objects.filter(vehicule_id=id)
    consommations=Consommation.objects.filter(vehicule_id=id)
    total_consommation=Consommation.objects.filter(vehicule_id=id).aggregate(Sum("montant", default=0))

    types=Type.objects.all()
    type_entretiens=Type_entretien.objects.all()

    graphic_consommation=stat_consonsommation(id)
    
    return render(
        request, "print/vehicule.html", 
        {
            "vehicules":vehicules, "vehicule": vehicule, "pannes":pannes, "entretiens": entretiens, "consommations":consommations,
            "total_consommation": total_consommation, "types":types, "type_entretiens":type_entretiens,
            "graphic_consommation":graphic_consommation,
        }
    )

def maps(request, id):
    vehicule=Vehicule.objects.get(id=id)
    vehicules=Vehicule.objects.all()
    pannes=Panne.objects.filter(vehicule_id=id)

    f = open('data.json')
    data = json.load(f)
    df=pd.DataFrame(data)
    f.close()
    
    locations = [
        [
            (38.893596444352134, -77.03814983367920),
            (38.893379333722040, -77.03792452812195),
        ],
        [
            (38.893379333722040, -77.03792452812195),
            (38.893162222428310, -77.03761339187622),
        ],
        [
            (38.893162222428310, -77.03761339187622),
            (38.893028615148424, -77.03731298446655),
        ],
        [
            (38.893028615148424, -77.03731298446655),
            (38.892920059048464, -77.03691601753235),
        ],
        [
            (38.892920059048464, -77.03691601753235),
            (38.892903358095296, -77.03637957572937),
        ],
        [
            (38.892903358095296, -77.03637957572937),
            (38.893011914220770, -77.03592896461487),
        ],
        [
            (38.893011914220770, -77.03592896461487),
            (38.893162222428310, -77.03549981117249),
        ],
        [
            (38.893162222428310, -77.03549981117249),
            (38.893404384982480, -77.03514575958252),
        ],
        [
            (38.893404384982480, -77.0351),
            (38.893596444352134, -77.03496336936950),
        ],
    ]

    print(df)
    #df['lat'].iloc[0], df['lng'].iloc[0] 
    
    m=folium.Map(location=[38.893596444352134, -77.03814983367920], zoom_start=15, titles="Parcours")
    '''coordinates=[]
    for index, row in df.iterrows():
        folium.Marker([row["lat"], row["lng"]], popup="Ici", tooltip="Clicquer...").add_to(m)
        coordinates.append((row["lat"], row["lng"]))
    '''
    folium.PolyLine(
        locations=locations,
        color="blue",
        weight=5,
        opacity=1,
        smooth_factor=0,
    ).add_to(m)

    return render(request, "print/maps.html", {"maps": m._repr_html_(), "vehicules":vehicules, "vehicule": vehicule} )


def stat_consonsommation(vehicule_id):
    query=Consommation.objects.filter(vehicule_id=vehicule_id).order_by('date').values()
    data=[]
    try:
        for row in query:
            k=[row["date"].strftime("%d/%m/%Y"), row["montant"]]
            data.append(k)

        df=pd.DataFrame(query, index=data['date'])
        plt.figure()
        df.plot(kind='line') #.groupby('structure').count()
        file_name='consommation_graphic.png'
        plt.title("Graphique de consommation")
        plt.savefig(file_name)
        file_url='stats/'+'consommation_graphic.png'
        shutil.move(file_name, "static/"+file_url)
        return 'stats/'+file_name
    except:
        return False