from django.contrib import admin
from django.urls import path
from . import views, PosteC

urlpatterns = [
    path('',views.index, name='list_employe'),
    path('save/<int:id>',views.save, name='save_employe'),
    path('delete/<int:id>',views.delete, name='delete_employe'),

    path('poste',PosteC.index, name='list_poste'),
    path('poste/save/<int:id>',PosteC.save, name='save_poste'),
    path('poste/delete/<int:id>',PosteC.delete, name='delete_poste'),
]
