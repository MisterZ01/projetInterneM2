from django.shortcuts import render



# accueil
def index(request):
    return render(request, 'index.html')
# client
def Client_create(request):
    return render(request, 'pages/Clients/creer.html')

def Client_list(request):
    return render(request, 'pages/Clients/liste.html')

# panneaux
def Panneau_create(request):
    return render(request, 'pages/Panneaux/creer.html')

def Panneau_list(request):
    return render(request, 'pages/Panneaux/liste.html')

# contrat
def Contrat_create(request):
    return render(request, 'pages/Contrats/creer.html')

def Contrat_list(request):
    return render(request, 'pages/Contrats/liste.html')