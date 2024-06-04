from django.shortcuts import render, redirect
from .models import Poste, Employe
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request):
    postes=Poste.objects.all()
    data=Employe.objects.all()
    return render(request, 'employe/list.html',{'data':data, 'postes':postes})

@is_admin
def save(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Employe.objects.get(id=id)
        else:
            obj=Employe()
        obj.matricule=request.POST.get('matricule')
        obj.nom=request.POST.get('nom')
        obj.prenom=request.POST.get('prenom')
        obj.date_naissance=request.POST.get('date_naissance')
        obj.lieu_naissance=request.POST.get('lieu_naissance')
        obj.poste_id=int(request.POST.get('poste'))
        obj.save()

    return redirect('list_employe')

@is_admin
def delete(request, id):
    employe=Employe.objects.get(id=id)
    employe.delete()
    return redirect('list_employe')
