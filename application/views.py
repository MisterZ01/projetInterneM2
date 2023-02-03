from django.shortcuts import render
import requests



# accueil
def index(request):
    return render(request, 'index.html')
# client
def Client_create(request):
    return render(request, 'pages/Clients/creer.html')

def Client_list(request):
    reponse = requests.get("http://127.0.0.1:8000/api/clients").json()
    return render(request, 'pages/Clients/liste.html',{'data':reponse})

def Client_detail(request, id):
    link = "http://127.0.0.1:8000/api/clients/"+str(id)
    reponse = requests.get(link).json()
    print(link)
    return render(request, 'pages/Clients/detail.html', {'data':reponse})

def Client_edit(request, id):
    link = "http://127.0.0.1:8000/api/clients/"+str(id)+"/edit"
    reponse = requests.get(link).json()
    return render(request, 'pages/Panneaux/usageapi.html', {'data':reponse})

def Client_delete(request, id):
    r=  requests.post("http://127.0.0.1:8000/api/client/clients/{id}").json()
    return render(request, "a")

# panneaux
def Panneau_create(request):
    
    return render(request, 'pages/Panneaux/creer.html')

def Panneau_list(request):
    reponse = requests.get("http://127.0.0.1:8000/api/panneaus").json()
    return render(request, 'pages/Panneaux/liste.html',{'data':reponse})

# contrat
def Contrat_create(request):
    return render(request, 'pages/Contrats/creer.html')

def Contrat_list(request):
    reponse = requests.get("http://127.0.0.1:8000/api/contrats").json()
    return render(request, 'pages/Contrats/liste.html',{'data':reponse})


# ---------------------------------------------- projet odc test api ----------------------------
# test de mon api
def usageapi(request):
    reponse1 = requests.get("http://127.0.0.1:8000/api/clients").json()

    return render(request, 'pages/Panneaux/usageapi.html', {'data':reponse1})


