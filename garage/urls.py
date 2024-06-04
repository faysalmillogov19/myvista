from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='list_garage'),
    path('save/<int:id>',views.save, name='save_garage'),
    path('delete/<int:id>',views.delete, name='delete_garage'),
]
