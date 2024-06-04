from django.contrib import admin
from django.urls import path
from . import views, DevisC

urlpatterns = [
    path('<int:vehicule>',views.index, name='list_panne'),
    path('save/<int:id>',views.save, name='save_panne'),
    path('delete/<int:id>',views.delete, name='delete_panne'),

    path('devis/<int:panne>',DevisC.index, name='list_devis'),
    path('devis/save/<int:id>',DevisC.save, name='save_devis'),
    path('devis/delete/<int:id>',DevisC.delete, name='delete_devis'),
]
