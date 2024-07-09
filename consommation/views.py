from django.shortcuts import render, redirect
from .models import Consommation
from vehicule.models import Vehicule
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request, vehicule):
    vehicule=Vehicule.objects.get(id=vehicule)
    data=Consommation.objects.filter(vehicule_id=vehicule)
    return render(request, 'consommation/list.html',{'data':data, 'vehicule':vehicule})

@is_admin
def save(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Consommation.objects.get(id=id)
        else:
            obj=Consommation()
            obj.vehicule_id=int(request.POST.get('vehicule'))
        obj.date=request.POST.get('date')
        obj.montant=request.POST.get('montant')
        obj.save()

    return redirect('print_infos_vehicule', id=obj.vehicule_id)

@is_admin
def delete(request, id):
    consommation=Consommation.objects.get(id=id)
    vehicule=consommation.vehicule_id
    consommation.delete()
    return redirect('print_infos_vehicule', id=vehicule)


