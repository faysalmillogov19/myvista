from django.shortcuts import render, redirect
from vehicule.models import Vehicule, Marque, Categorie, Carburant, Type as Type_vehicule
from panne.models import Panne, Devis, Type
from consommation.models import Consommation
from entretien.models import Entretien, Type_entretien
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from django.middleware.csrf import get_token
import datetime

from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

######################################################
##################  MODEL LIST   #####################
######################################################

@api_view(['GET'])
#@authentication_classes([SessionAuthentication, BasicAuthentication])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_vehicule(request):
    user_id=request.user.id
    query = Vehicule.objects.filter(proprio_id=user_id, desactivate=False)
    output=[]
    for data in query:
        output.append(
            {
            "id": data.id, 'immatriculation_vehicule':data.immatriculation, 'modele':data.modele, "date": data.date, "marque_id": data.marque.id,
            'marque_libelle':data.marque.libelle, "type_id": data.type.id, "type_libelle":data.type.libelle, 'categorie_id':data.categorie.id,
            'categorie_libelle':data.categorie.libelle, 'carburant_id':data.carburant.id, 'carburant_libelle':data.carburant.libelle,
            }
        )
    
    return Response(output)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_panne(request, vehicule):
    data = Panne.objects.filter(vehicule_id=vehicule)
    output=[]
    for query in data:
        output.append(
            {
                'id': query.id, 'pieces': query.pieces, 'description':query.description, 'date':query.date,
                'type_panne':query.type.libelle, 'type_panne_id':query.type_id,'immobile':int(query.immobile),
                'vehicule_id':query.vehicule_id, 'immatriculation_vehicule':query.vehicule.immatriculation, 'modele_vehicule':query.vehicule.modele,
                'marque_vehicule':query.vehicule.marque.libelle
            }
        )
    
    return Response(output)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_consommation(request, vehicule):
    data = Consommation.objects.filter(vehicule_id=vehicule)
    output=[]
    for query in data:
        output.append(
            {
                'id': query.id, 'date': query.date, 'montant':query.montant,
                'vehicule_id':query.vehicule_id, 'immatriculation_vehicule':query.vehicule.immatriculation, 'modele_vehicule':query.vehicule.modele,
                'marque_vehicule':query.vehicule.marque.libelle
            }
        )
    
    return Response(output)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_typepanne(request):
    data = Type.objects.all()
    output=[]
    for query in data:
        output.append({'id': query.id, 'libelle': query.libelle})
    
    return Response(output)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_type_entretien(request):
    data = Type_entretien.objects.all()
    output=[]
    for query in data:
        output.append({'id': query.id, 'libelle': query.libelle, 'duree_moyenne':query.duree_moyenne })
    
    return Response(output)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_entretien(request, vehicule):
    data = Entretien.objects.filter(vehicule_id=vehicule)
    output=[]
    for query in data:
        output.append(
            {
                'id': query.id, 'description':query.description, 'date': query.date, 'montant':query.montant, 'nombre':query.nombre,
                'type_id':query.type_id, 'type_libelle':query.type.libelle, 'type_duree_moyenne': query.type.duree_moyenne,
                'vehicule_id':query.vehicule_id, 'immatriculation_vehicule':query.vehicule.immatriculation, 'modele_vehicule':query.vehicule.modele,
                'marque_vehicule':query.vehicule.marque.libelle
            }
        )
    
    return Response(output)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_type_vehicule(request):
    data = Type_vehicule.objects.all()
    output=[]
    for query in data:
        output.append({'id': query.id, 'libelle': query.libelle })
    
    return Response(output)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_categorie(request):
    data = Categorie.objects.all()
    output=[]
    for query in data:
        output.append({'id': query.id, 'libelle': query.libelle, "description": query.libelle })
    
    return Response(output)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_carburant(request):
    data = Carburant.objects.all()
    output=[]
    for query in data:
        output.append({'id': query.id, 'libelle': query.libelle })
    
    return Response(output)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_marque(request):
    data = Marque.objects.all()
    output=[]
    for query in data:
        output.append({'id': query.id, 'libelle': query.libelle })
    
    return Response(output)


########################################################
#################### GET INFO ##########################
########################################################

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_vehicule(request, id):
    try:
        data = Vehicule.objects.get(id=id)
        output={
            "id": data.id, 'immatriculation_vehicule':data.immatriculation, 'modele':data.modele, "date": data.date, "marque_id": data.marque.id,
            'marque_libelle':data.marque.libelle, "type_id": data.type.id, "type_libelle":data.type.libelle, 'categorie_id':data.categorie.id,
            'categorie_libelle':data.categorie.libelle, 'carburant_id':data.carburant.id, 'carburant_libelle':data.carburant.libelle,
        }
    except Exception as e:
        output={}
        
    
    return Response(output)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_panne(request, id):
    try:
        data = Panne.objects.get(id=id)
        output={
                'id': data.id, 'pieces': data.pieces, 'description':data.description, 'date':data.date,
                'type_panne':data.type.libelle, 'type_panne_id':data.type_id,'immobile':int(data.immobile),
                'vehicule_id':data.vehicule_id, 'immatriculation_vehicule':data.vehicule.immatriculation, 'modele_vehicule':data.vehicule.modele,
                'marque_vehicule':data.vehicule.marque.libelle
            }
    except Exception as e:
        output={}
        
    
    return Response(output)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_typepanne(request, id):
    
    try:
        data = Type.objects.get(id=id)
        output={'id': data.id, 'libelle': data.libelle}
    except Exception as e:
        output={}
    
    return Response(output)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_consommation(request, id):
    
    try:
        data = Consommation.objects.get(id=id)
        output={
                'id':data.id, 'date': data.date, 'montant': data.montant,
                'vehicule_id':data.vehicule_id, 'immatriculation_vehicule':data.vehicule.immatriculation, 'modele_vehicule':data.vehicule.modele,
                'marque_vehicule':data.vehicule.marque.libelle
        }
    except Exception as e:
        output={}
    
    return Response(output)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_type_entretien(request, id):
    
    try:
        data = Type_entretien.objects.get(id=id)
        output={'id': data.id, 'libelle': data.libelle, 'duree_moyenne':data.duree_moyenne}
    except Exception as e:
        output={}
    
    return Response(output)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_entretien(request, id):
    
    try:
        query = Entretien.objects.get(id=id)
        output={
                'id': query.id, 'description':query.description, 'date': query.date, 'montant':query.montant, 'nombre':query.nombre,
                'type_id':query.type_id, 'type_libelle':query.type.libelle, 'type_duree_moyenne': query.type.duree_moyenne,
                'vehicule_id':query.vehicule_id, 'immatriculation_vehicule':query.vehicule.immatriculation, 'modele_vehicule':query.vehicule.modele,
                'marque_vehicule':query.vehicule.marque.libelle
       }
    except Exception as e:
        output={}
    
    return Response(output)




########################################################
####################    SAVE      ######################
########################################################


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def save_vehicule(request, id):
    id=int(id)
    data={'reponse':0}
    if id>0:
        obj=Vehicule.objects.get(id=id)
    else:
        obj=Vehicule()
        obj.proprio_id=request.user.id
        obj.desactivate=False
    try:
        obj.immatriculation=request.POST.get('immatriculation')
        obj.modele=request.POST.get('modele')
        if request.POST.get('date'):
            obj.date=datetime.datetime.strptime(request.POST.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        if int(request.POST.get('categorie')):
            obj.categorie_id=int(request.POST.get('categorie'))


        if request.POST.get('marque'):
            saisie=str(request.POST.get('marque')).lower()
            marque=Marque.objects.filter(libelle__icontains=saisie).first()
            if marque is None:
                marque=Marque()
                marque.libelle= request.POST.get('marque')
                marque.save()

            obj.marque=marque
        if int( request.POST.get('type') ):
            obj.type_id=int(request.POST.get('type'))
        if request.POST.get('carburant'):
            obj.carburant_id=int(request.POST.get('carburant'))
        obj.save()
        data={'response':1}
    except Exception as e:
        data={'response':-1}
    
    return Response(data)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def save_panne(request, id):
    id=int(id)
    data={'reponse':0}
    if id>0:
        obj=Panne.objects.get(id=id)
    else:
        obj=Panne()
    try:
        obj.pieces=request.POST.get('piece')
        obj.description=request.POST.get('description')
        obj.date=datetime.datetime.strptime(request.POST.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        obj.type_id=int(request.POST.get('type'))
        obj.vehicule_id=int(request.POST.get('vehicule'))
        obj.immobile=bool(request.POST.get('immobile'))
        obj.save()
        data={'response':1}
    except Exception as e:
        data={'response':-1}
    
    return Response(data)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def save_consommation(request, id):
    data={'reponse':0}
    if id>0:
        obj=Consommation.objects.get(id=id)
    else:
        obj=Consommation()
        
    try:
        obj.montant=int(request.POST.get('montant'))
        obj.date=datetime.datetime.strptime(request.POST.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        obj.vehicule_id=int(request.POST.get('vehicule'))
        obj.save()
        data={'response':1}
    except Exception as e:
        data={'response':-1}
    
    return Response(data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def save_entretien(request, id):
    data={'reponse':0}
    if id>0:
        obj=Entretien.objects.get(id=id)
    else:
        obj=Entretien()
        
    try:
        obj.description=str(request.POST.get('description'))
        obj.montant=float(request.POST.get('montant'))
        obj.nombre=float(request.POST.get('nombre'))
        obj.date=datetime.datetime.strptime(request.POST.get('date'), '%d/%m/%Y').strftime('%Y-%m-%d')
        obj.vehicule_id=int(request.POST.get('vehicule'))
        obj.type_id=int(request.POST.get('type'))
        obj.save()
        data={'response':1}
    except Exception as e:
        data={'response':-1}
    
    return Response(data)

#########################################################
#####################   DELETE   ########################
#########################################################

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def desactive_vehicule(request, id):
    try:
        obj=Vehicule.objects.get(id=id)
        obj.desactivate=True
        obj.save()
        data={'response':1}
    except Exception as e:
        data={'response':-1}
    return Response(data)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def active_vehicule(request, id):
    try:
        obj=Vehicule.objects.get(id=id)
        obj.desactivate=False
        obj.save()
        data={'response':1}
    except Exception as e:
        data={'response':-1}
    return Response(data)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_panne(request, id):
    try:
        panne=Panne.objects.get(id=id)
        panne.delete()
        data={'response':1}
    except Exception as e:
        data={'response':-1}
    return Response(data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_consommation(request, id):
    try:
        obj=Consommation.objects.get(id=id)
        obj.delete()
        data={'response':1}
    except Exception as e:
        data={'response':-1}
    return Response(data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_entretien(request, id):
    try:
        obj=Entretien.objects.get(id=id)
        obj.delete()
        data={'response':1}
    except Exception as e:
        data={'response':-1}
    return Response(data)