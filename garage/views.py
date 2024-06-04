from django.shortcuts import render, redirect
from .models import Garage
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request):
    data=Garage.objects.all()
    return render(request,'garage/list.html',{'data':data})

@is_admin
def save(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Garage.objects.get(id=id)
        else:
            obj=Garage()
        obj.denomination=request.POST.get('denomination')
        obj.telephone=request.POST.get('telephone')
        obj.email=request.POST.get('email')
        obj.bp=request.POST.get('bp')
        obj.save()
    
    return redirect('list_garage')

@is_admin
def delete(request, id):
    Garage.objects.get(id=id).delete()
    return redirect('list_garage')

