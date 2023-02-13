from django.shortcuts import render
import requests, json
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages


# accueil
def index(request):
    nbclienttab = requests.get("http://127.0.0.1:9000/api/clients").json()
    nbclient = nbclienttab["results"]

    nbcontrattab  = requests.get("http://127.0.0.1:9000/api/contrats").json()
    nbcontrat = nbcontrattab["results"]

    nbpanneautab  = requests.get("http://127.0.0.1:9000/api/panneaus").json()
    nbpanneau = nbpanneautab["results"]

    return render(request, 'index.html',{'nbclient':nbclient, 'nbcontrat': nbcontrat, 'nbpanneau': nbpanneau })
# client ----------------------------------------------------------------------------------------
def Client_create(request):
    edit=False
    return render(request, 'pages/Clients/creer.html', {'edit':edit})

@csrf_exempt
def Client_store(request):

    nom_client=request.POST['nom_client']
    prenom_client=request.POST['prenom_client']
    email_client=request.POST['email_client']
    entreprise_client=request.POST['entreprise_client']

    if request.POST['id']=="":
        password_client=request.POST['password_client']
        url ="http://127.0.0.1:8000/api/clients"

        reponse=requests.post(url,data={
            "nom_client":request.POST['nom_client'],
            "prenom_client":request.POST['prenom_client'],
            "email_client":request.POST['email_client'],
            "entreprise_client":request.POST['entreprise_client'],
            "password_client":request.POST['password_client']
        })
        messages.success(request, " Client enrégistré avec succès ")
        return render(request, 'pages/Clients/creer.html',{'data':reponse})
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
        messages.success(request, " Client modifié avec succès ")
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
    messages.success(request, " Client supprimé avec succès ")
    return render(request, 'pages/Clients/liste.html',{'data':reponse, 'reponse_del_req':reponse_del_req})

# panneaux ------------------------------------------------------------------------------------

def Panneau_create(request):

    return render(request, 'pages/Panneaux/creer.html')

def Panneau_list(request):
    reponse = requests.get("http://127.0.0.1:8000/api/panneaus").json()
    return render(request, 'pages/Panneaux/liste.html',{'data':reponse})
@csrf_exempt
def Panneau_store(request):
    nom_panneau=request.POST['nom_panneau']
    latitude=request.POST['latitude']
    longitude=request.POST['longitude']
    print(request.POST['client_id'])
    # if request.POST['client_id'] !=" ":
    url ="http://127.0.0.1:8000/api/panneaus"

    rep = requests.post(url,data={
        "nom_panneau":request.POST['nom_panneau'],
        "latitude":request.POST['latitude'],
        "longitude":request.POST['longitude'],
        "client_id" :request.POST['client_id']
    }).json()
    print(rep)
    return render(request, 'pages/Contrats/creer.html')
    


# contrat --------------------------------------------------------------------------------------

def Contrat_create(request):
    reponse = requests.get("http://127.0.0.1:8000/api/clients").json()
    return render(request, 'pages/Contrats/creer.html',{'data':reponse})

def Contrat_list(request):
    reponse = requests.get("http://127.0.0.1:8000/api/contrats").json()
    print(reponse)
    return render(request, 'pages/Contrats/liste.html',{'data':reponse})

@csrf_exempt
def Contrat_store(request):
    nom_contrat=request.POST['nom_contrat']
    dateDebut=request.POST['dateDebut']
    dateFin=request.POST['dateFin']
    print(request.POST['client_id'])
    # if request.POST['client_id'] !=" ":
    url ="http://127.0.0.1:8000/api/contrats"

    rep = requests.post(url,data={
        "nom_contrat":request.POST['nom_contrat'],
        "dateDebut":request.POST['dateDebut'],
        "dateFin":request.POST['dateFin'],
        "client_id" :request.POST['client_id']
    }).json()
    messages.success(request, " Contrat enrégistré avec succès ")
    return render(request, 'pages/Contrats/creer.html')
    # else:
    #     id = request.POST['client_id']
    #     url ="http://127.0.0.1:8000/api/contrats/"+str(id)
    #     url = url.replace(" ", "")
    #     Data= {

    #         "nom_contrat":request.POST['nom_contrat'],
    #         "dateDebut":request.POST['dateDebut'],
    #         "dateFin":request.POST['dateFin'],
    #         "client_id" :request.POST['client_id']
    #     }

    #     rep = requests.put(url,data={
    #         "nom_contrat":request.POST['nom_contrat'],
    #         "dateDebut":request.POST['dateDebut'],
    #         "dateFin":request.POST['dateFin'],
    #         "client_id" :request.POST['client_id']
    #     })
    #     return render(request, 'pages/Contrats/creer.html')

def Contrat_delete(request, id):
    link = "http://127.0.0.1:8000/api/contrats/"+str(id)
    reponse_del_req = requests.delete(link).json()
    reponse = requests.get("http://127.0.0.1:8000/api/contrats").json()
    messages.success(request, " Contrat supprimé avec succès ")
    return render(request, 'pages/Contrats/liste.html',{'data':reponse, 'reponse_del_req':reponse_del_req})

def Contrat_detail(request, id):
    link = "http://127.0.0.1:8000/api/contrats/"+str(id)
    reponse = requests.get(link).json()
    print(reponse)
    return render(request, 'pages/Contrats/detail.html', {'data':reponse})


# ---------------------------------------------- projet odc test api ----------------------------
# test de mon api
def usageapi(request):
    reponse1 = requests.get("http://127.0.0.1:8000/api/clients").json()

    return render(request, 'pages/Panneaux/usageapi.html', {'data':reponse1})

# test requette ajax
def pageTestAjaxt(request):
    reponse1 = requests.get("http://127.0.0.1:8000/api/clients").json()
    return render(request, 'pages/Clients/testAjax.html', {'data':reponse1})

@csrf_exempt
def Ajax_lient_store(request):

    nom_client=request.POST['nom_client']
    prenom_client=request.POST['prenom_client']
    email_client=request.POST['email_client']
    entreprise_client=request.POST['entreprise_client']
    if request.POST['id']=="":
        password_client=request.POST['password_client']
        url ="http://127.0.0.1:8000/api/clients"

        requests.post(url,data={
            "nom_client":request.POST['nom_client'],
            "prenom_client":request.POST['prenom_client'],
            "email_client":request.POST['email_client'],
            "entreprise_client":request.POST['entreprise_client'],
            "password_client":request.POST['password_client']
        })
        reponse = requests.get("http://127.0.0.1:8000/api/clients").json()
        return render(request,{'data':reponse})
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

def Ajax_edit(request, id):
    link = "http://127.0.0.1:8000/api/clients/"+str(id)
    reponse = requests.get(link).json()
    edit=True
    for el in reponse:
        id_client=el["id"]
        nom_client=el["nom_client"]
        prenom_client=el["prenom_client"]
        email_client=el["email_client"]
        entreprise_client=el["entreprise_client"]
    # data = {nom_client, prenom_client,email_client,entreprise_client}
    return render(request, 'pages/Clients/testAjax.html', {
                                                        'edit':edit,
                                                        'id_client':id_client,
                                                        'nom_client':nom_client,
                                                        'prenom_client':prenom_client,
                                                        'email_client':email_client,
                                                        'entreprise_client':entreprise_client
                                                        })