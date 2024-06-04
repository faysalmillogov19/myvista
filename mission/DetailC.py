from django.shortcuts import render, redirect
from .models import Escale, Mission, Membre
from employe.models import Employe
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request, mission):
    mission=Mission.objects.get(id=mission)
    employes=Employe.objects.all()
    membres=Membre.objects.filter(mission_id=mission)
    escales=Escale.objects.filter(mission_id=mission)
    return render(request, 'details_mission/list.html',{'escales':escales, 'membres':membres, 'employes':employes, 'mission':mission})

@is_admin
def save_escale(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Escale.objects.get(id=id)
        else:
            obj=Escale()
        obj.date=request.POST.get('date')
        obj.destination=request.POST.get('destination')
        obj.mission_id=int(request.POST.get('mission'))
        obj.save()

    return redirect('details_mission', mission=obj.mission_id)

@is_admin
def delete_escale(request, id):
    escale=Escale.objects.get(id=id)
    mission=escale.mission_id
    escale.delete()
    return redirect('details_mission', mission=mission)

@is_admin
def save_membre(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Membre.objects.get(id=id)
        else:
            obj=Membre()
        obj.employe_id=int(request.POST.get('employe'))
        obj.mission_id=int(request.POST.get('mission'))
        obj.save()

    return redirect('details_mission', mission=obj.mission_id)

@is_admin
def delete_membre(request, id):
    membre=Membre.objects.get(id=id)
    mission=membre.mission_id
    membre.delete()
    return redirect('details_mission', mission=mission)

