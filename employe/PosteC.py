from django.shortcuts import render, redirect
from .models import Poste
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request):
    data=Poste.objects.all()
    return render(request, 'poste/list.html',{'data':data})

@is_admin
def save(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Poste.objects.get(id=id)
        else:
            obj=Poste()
        obj.libelle=request.POST.get('libelle')
        obj.save()

    return redirect('list_poste')

@is_admin
def delete(request, id):
    poste=Poste.objects.get(id=id)
    poste.delete()
    return redirect('list_poste')


