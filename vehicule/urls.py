from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='list_vehicule'),
    path('save/<int:id>',views.save, name='save_vehicule'),
    path('delete/<int:id>',views.delete, name='delete_vehicule'),

    path('list_vehicule/',views.list_vehicule, name='list_api_vehicule'),
]
