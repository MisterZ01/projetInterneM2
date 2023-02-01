from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('Client/create', views.Client_create, name="Client_create"),
    path('Client/list', views.Client_list, name="Client_list"),
    path('Contrat/create', views.Contrat_create, name="Contrat_create"),
    path('Contrat/list', views.Contrat_list, name="Contrat_list"),
    path('Panneau/create', views.Panneau_create, name="Panneau_create"),
    path('Panneau/list', views.Panneau_list, name="Panneau_list"),
    path('usageapi', views.usageapi, name="usageapi"),
    path('detail', views.detail, name="detail"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
]
