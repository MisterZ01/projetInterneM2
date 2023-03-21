from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.loginpage, name="login"),
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
    path('contrat/edit/<int:id>', views.Contrat_edit, name="Contrat_edit"),
    path('Contrat/detail/<int:id>', views.Contrat_detail, name="Contrat_detail"),
    path('Contrat/delete/<int:id>', views.Contrat_delete, name="Contrat_delete"),
    # path('Contrat/pdf', views.contrat_pdf, name="Contrat_pdf"),
    path('Contrat/pdf', views.GeneratePdf.as_view()),

    # debut panneau
    path('Panneau/create', views.Panneau_create, name="Panneau_create"),
    path('Panneau/list', views.Panneau_list, name="Panneau_list"),
    path('Panneau/store', views.Panneau_store, name="Panneau_store"),
    path('Panneau/edit/<int:id>', views.Panneau_edit, name="Panneau_edit"),
    path('Panneau/detail/<int:id>', views.Panneau_detail, name="Panneau_detail"),
    path('Panneau/delete/<int:id>', views.Panneau_delete, name="Panneau_delete"),
    path('Panneau/desallouer/<int:id>', views.Panneau_desallouer, name="Panneau_desallouer"),
    path('Panneau/allouer', views.Panneau_allouer, name="Panneau_allouer"),


    path('usageapi', views.usageapi, name="usageapi"),
    path('pageTestAjaxt', views.pageTestAjaxt, name="pageTestAjaxt"),
    path('Ajax_lient_store', views.Ajax_lient_store, name="Ajax_lient_store"),
    path('Ajax_edit/<int:id>', views.Ajax_edit, name="Ajax_edit"),

]
