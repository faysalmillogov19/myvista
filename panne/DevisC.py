from django.shortcuts import render, redirect
from .models import Type, Devis, Panne
from garage.models import Garage
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
import os
from django.conf import settings
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request, panne):
    panne=Panne.objects.get(id=panne)
    garages=Garage.objects.all()
    data=Devis.objects.filter(panne_id=panne)
    return render(request, 'devis/list.html',{'data':data, 'garages':garages, 'panne':panne})

@is_admin
def save(request, id):
    
    if request.method=='POST':
        if id>0:
            obj=Devis.objects.get(id=id)
        else:
            obj=Devis()
        obj.cout_devis=float(request.POST.get('cout_devis'))
        if request.POST.get('cout_reparation'):
            obj.cout_reparation=float(request.POST.get('cout_reparation'))
        obj.date_devis=request.POST.get('date_devis')
        if request.POST.get('date_reparation'):
            obj.date_reparation=request.POST.get('date_reparation')
        obj.panne_id=int(request.POST.get('panne'))
        obj.garage_id=int(request.POST.get('garage'))
        obj.accepter=bool(request.POST.get('accepter'))
        if request.FILES.get('proforma'):
            if obj.proforma:
                os.remove(os.path.join(settings.MEDIA_ROOT, obj.proforma.name))
            obj.proforma=request.FILES.get('proforma')
        if request.FILES.get('facture'):
            if obj.facture:
                os.remove(os.path.join(settings.MEDIA_ROOT, obj.facture.name))
            obj.facture=request.FILES.get('facture')
        obj.save()

    return redirect('list_devis', panne=obj.panne_id)

@is_admin
def delete(request, id):
    devis=Devis.objects.get(id=id)
    panne=devis.panne_id
    if devis.proforma:
        os.remove(os.path.join(settings.MEDIA_ROOT, devis.proforma.name))
    if devis.facture:
        os.remove(os.path.join(settings.MEDIA_ROOT, devis.facture.name))
    devis.delete()
    return redirect('list_devis', panne=panne)


