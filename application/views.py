from django.shortcuts import render
import requests



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


# ---------------------------------------------- projet odc test api ----------------------------
# test de mon api
def usageapi(request):
    reponse = requests.get("http://127.0.0.1:8000/api/all").json()
    return render(request, 'pages/Panneaux/usageapi.html', {'data':reponse})
# detail
def detail(request, id):
    reponse = requests.get("http://127.0.0.1:8000/api/all").json()
    return render(request, 'pages/Panneaux/usageapi.html', {'data':reponse})
# edit
def edit(request, id):
    reponse = requests.post("http://127.0.0.1:8000/api//update/{id}").json()
    return render(request, 'pages/Panneaux/usageapi.html', {'data':reponse})
# delete
def delete(request, id):
    r=  requests.post("http://127.0.0.1:8000/api/item/1/delete").json()
    return render(request, "a")
