from django.shortcuts import render, redirect
from .models import Mission
from employe.models import Employe
from vehicule.models import Vehicule
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request):
    employes=Employe.objects.all()
    vehicules=Vehicule.objects.all()
    data=Mission.objects.all()
    return render(request, 'mission/list.html',{'data':data, 'employes':employes, 'vehicules':vehicules})

@is_admin
def save(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Mission.objects.get(id=id)
        else:
            obj=Mission()
        obj.debut=request.POST.get('debut')
        obj.fin=request.POST.get('fin')
        obj.depart=request.POST.get('depart')
        obj.destination=request.POST.get('destination')
        obj.vehicule_id=int(request.POST.get('vehicule'))
        obj.save()

    return redirect('list_mission')

@is_admin
def delete(request, id):
    mission=Mission.objects.get(id=id)
    mission.delete()
    return redirect('list_mission')


