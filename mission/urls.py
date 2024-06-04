from django.contrib import admin
from django.urls import path
from . import views, DetailC

urlpatterns = [
    path('',views.index, name='list_mission'),
    path('save/<int:id>',views.save, name='save_mission'),
    path('delete/<int:id>',views.delete, name='delete_mission'),

    path('details/<int:mission>',DetailC.index, name='details_mission'),
    
    path('save/escale/<int:id>',DetailC.save_escale, name='save_escale'),
    path('delete/escale/<int:id>',DetailC.delete_escale, name='delete_escale'),

    
    path('save/membre/<int:id>',DetailC.save_membre, name='save_membre'),
    path('delete/membre/<int:id>',DetailC.delete_membre, name='delete_membre'),

]
