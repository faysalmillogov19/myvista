from django.shortcuts import render, redirect
from .models import Entretien, Type_entretien
from vehicule.models import Vehicule
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request, vehicule):
    types=Type_entretien.objects.all()
    data=Entretien.objects.filter(vehicule_id=vehicule)
    return render(request, 'entretien/list.html',{'data':data, 'types':types, 'vehicule':vehicule})

@is_admin
def save(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Entretien.objects.get(id=id)
        else:
            obj=Entretien()
        obj.description=request.POST.get('description')
        obj.date=request.POST.get('date')
        if request.POST.get('nombre'):
            obj.nombre=float(request.POST.get('nombre'))
        if request.POST.get('montant'):
            obj.montant=float(request.POST.get('montant'))
        obj.vehicule_id=int(request.POST.get('vehicule'))
        obj.type_id=int(request.POST.get('type'))
        obj.save()

    return redirect('liste_entretien', vehicule=obj.vehicule_id)

@is_admin
def delete(request, id):
    entretien=Entretien.objects.get(id=id)
    vehicule=entretien.vehicule_id
    entretien.delete()
    return redirect('liste_entretien', vehicule=vehicule)


