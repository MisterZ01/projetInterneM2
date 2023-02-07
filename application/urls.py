from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    # debut client
    path('Client/create', views.Client_create, name="Client_create"),
    path('Client/store', views.Client_store, name="Client_store"),
    path('Client/list', views.Client_list, name="Client_list"),
    path('detail/<int:id>', views.Client_detail, name="Client_detail"),
    path('edit/<int:id>', views.Client_edit, name="Client_edit"),
    path('delete/<int:id>', views.Client_delete, name="Client_delete"),

    # debut contrat
    path('Contrat/create', views.Contrat_create, name="Contrat_create"),
    path('Contrat/list', views.Contrat_list, name="Contrat_list"),
    path('Contrat/store', views.Contrat_store, name="Contrat_store"),
    path('Contrat/delete/<int:id>', views.Contrat_delete, name="Contrat_delete"),

    # debut panneau
    path('Panneau/create', views.Panneau_create, name="Panneau_create"),
    path('Panneau/list', views.Panneau_list, name="Panneau_list"),
    path('Panneau/store', views.Panneau_store, name="Panneau_store"),

    path('usageapi', views.usageapi, name="usageapi"),
]
