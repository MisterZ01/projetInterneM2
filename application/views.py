from django.shortcuts import render
import requests, json
from django.views.decorators.csrf import csrf_exempt



# accueil
def index(request):

    return render(request, 'index.html')
# client
def Client_create(request):
    edit=False
    return render(request, 'pages/Clients/creer.html', {'edit':edit})

@csrf_exempt
def Client_store(request):

    nom_client=request.POST['nom_client']
    prenom_client=request.POST['prenom_client']
    email_client=request.POST['email_client']
    entreprise_client=request.POST['entreprise_client']

    if request.POST['id']==" ":
        password_client=request.POST['password_client']
        url ="http://127.0.0.1:8000/api/clients"
        Data= {

            "nom_client":request.POST['nom_client'],
            'prenom_client':request.POST['prenom_client'],
            "email_client":request.POST['email_client'],
            "entreprise_client":request.POST['entreprise_client'],
            "password_client":request.POST['password_client']

        }

        requests.post(url,data={
            "nom_client":request.POST['nom_client'],
            "prenom_client":request.POST['prenom_client'],
            "email_client":request.POST['email_client'],
            "entreprise_client":request.POST['entreprise_client'],
            "password_client":request.POST['password_client']

        })

        return render(request, 'pages/Clients/creer.html')
    else:
        id = request.POST['id']
        url ="http://127.0.0.1:8000/api/clients/"+str(id)
        url = url.replace(" ", "")
        Data= {

            "nom_client":request.POST['nom_client'],
            'prenom_client':request.POST['prenom_client'],
            "email_client":request.POST['email_client'],
            "entreprise_client":request.POST['entreprise_client'],
            "password_client":request.POST['password_client']

        }

        rep = requests.put(url,data={
            "nom_client":request.POST['nom_client'],
            "prenom_client":request.POST['prenom_client'],
            "email_client":request.POST['email_client'],
            "entreprise_client":request.POST['entreprise_client'],
            "password_client":request.POST['password_client']

        })
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
    link = "http://127.0.0.1:8000/api/clients/"+str(id)
    reponse = requests.get(link).json()
    edit=True
    data ={}
    for el in reponse:
        id_client=el["id"]
        nom_client=el["nom_client"]
        prenom_client=el["prenom_client"]
        email_client=el["email_client"]
        entreprise_client=el["entreprise_client"]
    # data = {nom_client, prenom_client,email_client,entreprise_client}
    return render(request, 'pages/Clients/creer.html', {
                                                        'edit':edit,
                                                        'id_client':id_client,
                                                        'nom_client':nom_client,
                                                        'prenom_client':prenom_client,
                                                        'email_client':email_client,
                                                        'entreprise_client':entreprise_client
                                                        })

def Client_delete(request, id):
    link = "http://127.0.0.1:8000/api/clients/"+str(id)
    reponse_del_req = requests.delete(link).json()
    reponse = requests.get("http://127.0.0.1:8000/api/clients").json()
    return render(request, 'pages/Clients/liste.html',{'data':reponse, 'reponse_del_req':reponse_del_req})

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


