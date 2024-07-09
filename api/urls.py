from django.contrib import admin
from django.urls import path
from . import views, Login

urlpatterns = [

    #######################################
    ##############   AUTH        ##########
    ######################################
    path('signin', Login.signin),
    path('signup',Login.signup),
    path('signout', Login.signout),
  
    #######################################
    ###########  VEHICULE    ##############
    #######################################

    path('vehicule',views.list_vehicule),
    path('get_vehicule/<int:id>',views.get_vehicule),
    path('save_vehicule/<int:id>',views.save_vehicule),
    path('desactive_vehicule/<int:id>',views.desactive_vehicule),

    #####################################
    ############# PANNE #################
    #####################################
    path('pannes/<int:vehicule>',views.list_panne),
    path('get_panne/<int:id>',views.get_panne),
    path('save_panne/<int:id>',views.save_panne),
    path('delete_panne/<int:id>',views.delete_panne),

    #####################################
    ########## CONSOMMATION  ############
    #####################################
    path('consommation/<int:vehicule>',views.list_consommation),
    path('get_consommation/<int:id>',views.get_consommation),
    path('save_consommation/<int:id>',views.save_consommation),
    path('delete_consommation/<int:id>',views.delete_consommation),

    #####################################
    ###########   ENTRETIEN  ############
    #####################################
    path('entretien/<int:vehicule>',views.list_entretien),
    path('get_entretien/<int:id>',views.get_entretien),
    path('save_entretien/<int:id>',views.save_entretien),
    path('delete_entretien/<int:id>',views.delete_entretien),
    
    ########################################
    ############# TYPE DE PANNE  ###########
    ########################################
    path('type_panne/',views.list_typepanne),
    path('type_panne/<int:id>',views.get_typepanne),

    ########################################
    ############# TYPE D'ENTRETIEN  ###########
    ########################################
    path('type_entretien/',views.list_type_entretien),
    path('type_entretien/<int:id>',views.get_type_entretien),

    ########################################
    ############# TYPE VEHICULE  ###########
    ########################################
    path('type_vehicules/',views.list_type_vehicule),

    ########################################
    ############# Marques  #################
    ########################################
    path('marques/',views.list_marque),

    ########################################
    ############# Categories  ###########
    ########################################
    path('categories/',views.list_categorie),

    ########################################
    ############# Carburant  ###########
    ########################################
    path('energies/',views.list_carburant),

]
