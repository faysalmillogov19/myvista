from django.shortcuts import render, redirect
from .models import Vehicule, Marque, Categorie, Carburant, Type
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin
from django.http import JsonResponse
from django.core.serializers import serialize
import json

@is_admin
def index(request):
    data=Vehicule.objects.all()
    marques=Marque.objects.all()
    categories=Categorie.objects.all()
    carburants=Carburant.objects.all()
    types=Type.objects.all()
    return render(request,'vehicule/list.html',{'data':data, 'marques':marques, 'carburants':carburants, 'types':types, 'categories':categories})

@is_admin
def save(request, id):
    if request.method=='POST':
        if id>0:
            obj=Vehicule.objects.get(id=id)
        else:
            obj=Vehicule()
        obj.immatriculation=request.POST.get('immatriculation')
        obj.modele=request.POST.get('modele')
        obj.date=request.POST.get('date')
        obj.categorie_id=int(request.POST.get('categorie'))
        if request.POST.get('marque'):
            saisie=str(request.POST.get('marque')).lower()
            marque=Marque.objects.filter(libelle__icontains=saisie).first()
            if marque is None:
                marque=Marque()
                marque.libelle= request.POST.get('marque')
                marque.save()

            obj.marque=marque
        obj.type_id=int(request.POST.get('type'))
        obj.carburant_id=int(request.POST.get('carburant'))
        obj.save()

    return redirect('print_infos_vehicule', id=obj.id)

@is_admin
def delete(request, id):
    Vehicule.objects.get(id=id).delete()
    return redirect('print_recapitulatif')

@is_admin
def list_vehicule(request):
    books = Vehicule.objects.all()
    serialized_data = serialize("json", books, use_natural_foreign_keys=True)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, status=200, safe=False)