from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:vehicule>',views.index, name='list_consommation'),
    path('save/<int:id>',views.save, name='save_consommation'),
    path('delete/<int:id>',views.delete, name='delete_consommation'),
]
