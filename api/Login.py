from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from employe.models import Employe

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def signup(request):
	
	try:
		user=User.objects.create_user(username=request.POST.get("username"), email=request.POST.get("email"), password=request.POST.get("password"))
		user.first_name=request.POST.get("nom")
		user.is_active=True
		user.save()
		token, created = Token.objects.get_or_create(user=user)
		return Response({"token": "Token "+token.key, 'username':user.username, "email":user.email, "nom":user.first_name, "prenom":user.last_name})

	except Exception as e:
		return Response({"token": ''})
		

@api_view(['POST'])
def signin(request):
	
	email=request.POST.get('username')
	password=request.POST.get('password')
	user=authenticate(username=email, password=password)
	
	if user :
		token, created = Token.objects.get_or_create(user=user)
		return Response({"token": "Token "+token.key, 'username':user.username, "email":user.email, "nom":user.first_name, "prenom":user.last_name})
	else:
		return Response({'token': ''})
	

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def signout(request):
	try:
		Token.objects.filter(user=request.user).delete()
		return Response({'message':1})
	except Exception as e:
		return Response({'message':-1})