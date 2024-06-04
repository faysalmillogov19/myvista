from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
import datetime
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def is_client(views_func):
	def wrapper_func(request, *args, **kwargs):

		has_role=request.user.groups.filter(name="client").exists()
		is_admin=request.user.groups.filter(name="admin").exists()
		user_is_superadmin=request.user.is_superuser

		if not request.user.is_authenticated:
			return redirect('user_signin')
		elif has_role or is_admin or user_is_superadmin :
			return views_func(request, *args, **kwargs)
		else:
			return render(request,'User/access_forbiden.html')

	return wrapper_func

def is_employe(views_func):
	def wrapper_func(request, *args, **kwargs):

		has_role=request.user.groups.filter(name="employe").exists()
		is_admin=request.user.groups.filter(name="admin").exists()
		user_is_superadmin=request.user.is_superuser

		if not request.user.is_authenticated:
			return redirect('user_signin')
		elif has_role or is_admin or user_is_superadmin :
			return views_func(request, *args, **kwargs)
		else:
			return render(request,'User/access_forbiden.html')

	return wrapper_func

def is_admin(views_func):
	def wrapper_func(request, *args, **kwargs):

		user_is_superadmin=request.user.is_superuser
		is_admin=request.user.groups.filter(name="admin").exists()

		if not request.user.is_authenticated:
			return redirect('user_signin')
		elif user_is_superadmin or is_admin :
			return views_func(request, *args, **kwargs)
		else:
			return render(request,'User/access_forbiden.html')

	return wrapper_func


def is_superadmin(views_func):
	def wrapper_func(request, *args, **kwargs):

		user_is_superadmin=request.user.is_superuser

		if not request.user.is_authenticated:
			return redirect('user_signin')
		elif  user_is_superadmin :
			return views_func(request, *args, **kwargs)
		else:
			return render(request,'User/access_forbiden.html')

	return wrapper_func


