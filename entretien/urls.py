from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('<int:vehicule>',views.index, name='liste_entretien'),
    path('save/<int:id>',views.save, name='save_entretien'),
    path('delete/<int:id>',views.delete, name='delete_entretien'),

]
