from django.shortcuts import render, redirect
from SystemConf.Back_Control_Access import is_admin, is_client, is_employe, is_superadmin

@is_admin
def index(request):
    return render(request,'index.html')