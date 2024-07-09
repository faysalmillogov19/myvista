from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.recapitulatif, name='print_recapitulatif'),
    path('maps/<int:id>',views.maps, name='maps_card'),
    path('vehicule/<int:id>',views.vehicule, name='print_infos_vehicule'),


]
