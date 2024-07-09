from django.shortcuts import render, redirect
from .models import Type, Panne
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request, vehicule):
    types=Type.objects.all()
    data=Panne.objects.filter(vehicule_id=vehicule)
    return render(request, 'panne/list.html',{'data':data, 'types':types, 'vehicule':vehicule})

@is_admin
def save(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Panne.objects.get(id=id)
        else:
            obj=Panne()
            obj.vehicule_id=int(request.POST.get('vehicule'))
        obj.pieces=request.POST.get('pieces')
        obj.description=request.POST.get('description')
        obj.date=request.POST.get('date')
        obj.type_id=int(request.POST.get('type'))
        obj.immobile=bool(request.POST.get('immobile'))
        obj.save()

    return redirect('print_infos_vehicule', id=obj.vehicule_id)

@is_admin
def delete(request, id):
    panne=Panne.objects.get(id=id)
    vehicule=panne.vehicule_id
    panne.delete()
    return redirect('print_infos_vehicule', id=vehicule)


