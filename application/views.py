from django.shortcuts import render, redirect
import requests, json
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, date

# connexion et deconnexion

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            redirect('login')

    return render(request, 'Pages/Compte/login.html')

# accueil
def index(request):
    nbclienttab = requests.get("http://127.0.0.1:9000/api/clients").json()
    nbclient = nbclienttab["results"]

    nbcontrattab  = requests.get("http://127.0.0.1:9000/api/contrats").json()
    nbcontrat = nbcontrattab["results"]
    reponse = requests.get("http://127.0.0.1:8000/api/contrats").json()
    echeance = 0
    for el in reponse:
        debut  = el['dateDebut']
        fin  = el['dateFin']
        debut = datetime.strptime(debut, '%Y-%m-%d')
        fin = datetime.strptime(fin, '%Y-%m-%d')
        if debut>fin :
            echeance +=1

    nbpanneautab  = requests.get("http://127.0.0.1:9000/api/panneaus").json()
    nbpanneau = nbpanneautab["results"]

    nbpanneaulibres  = requests.get("http://127.0.0.1:8000/api/panneaus/libre/count").json()

    return render(request, 'index.html',{'echeance':echeance,'nbclient':nbclient, 'nbcontrat': nbcontrat, 'nbpanneau': nbpanneau, 'nbpanneaulibres': nbpanneaulibres  })
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

        a=requests.post(url,data={
            "nom_client":request.POST['nom_client'],
            "prenom_client":request.POST['prenom_client'],
            "email_client":request.POST['email_client'],
            "entreprise_client":request.POST['entreprise_client'],
            "password_client":request.POST['password_client']
        })
        dat = {
            "nom_client":request.POST['nom_client'],
            "prenom_client":request.POST['prenom_client'],
            "email_client":request.POST['email_client'],
            "entreprise_client":request.POST['entreprise_client'],
            "password_client":request.POST['password_client']
        }

        messages.success(request, " Client enrégistré avec succès ")
        return redirect('Client_list')
    else:
        id = request.POST['id']
        url ="http://127.0.0.1:8000/api/clients/"+str(id)
        url = url.replace(" ", "")

        rep = requests.put(url,data={
            "nom_client":request.POST['nom_client'],
            "prenom_client":request.POST['prenom_client'],
            "email_client":request.POST['email_client'],
            "entreprise_client":request.POST['entreprise_client'],
            "password_client":request.POST['password_client']

        })
        messages.success(request, " Client modifié avec succès ")
        return redirect('Client_create')


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
    return redirect('Client_list')

# panneaux ------------------------------------------------------------------------------------

def Panneau_create(request):
    reponse = requests.get("http://127.0.0.1:8000/api/contrats").json()
    return render(request, 'pages/Panneaux/creer.html', {'data':reponse})

def Panneau_list(request):
    reponse = requests.get("http://127.0.0.1:8000/api/panneaus").json()
    return render(request, 'pages/Panneaux/liste.html',{'data':reponse})
@csrf_exempt
def Panneau_store(request):

    if request.GET['id_panneau']=="":
        url ="http://127.0.0.1:8000/api/panneaus"
        requests.post(url,data={
            "nom_panneau" :request.GET['nom_panneau'],
            "latitude" :request.GET['latitude'],
            "longitude" :request.GET['longitude'],
            "contrat_id" :request.GET['contrat_id']
        })

        messages.success(request, " Panneau enrégistré avec succès ")
        return redirect('Panneau_create')
    else:
        id = request.GET['id_panneau']
        url ="http://127.0.0.1:8000/api/panneaus/"+str(id)
        url = url.replace(" ", "")
        requests.put(url, data={
            "nom_panneau" :request.GET['nom_panneau'],
            "latitude" :request.GET['latitude'],
            "longitude" :request.GET['longitude']
        })
        messages.success(request, " Panneau modifié avec succès ")
        return redirect('Panneau_list')


def Panneau_detail(request, id):
    link = "http://127.0.0.1:8000/api/panneaus/"+str(id)
    reponse = requests.get(link).json()
    return render(request, 'pages/Panneaux/detail.html', {'data':reponse})

def Panneau_edit(request, id):
    link = "http://127.0.0.1:8000/api/panneaus/"+str(id)
    reponse = requests.get(link).json()
    edit=True
    for el in reponse:
        id_panneau=el["id"]
        nom_panneau=el["nom_panneau"]
        longitude=el["longitude"]
        latitude=el["latitude"]
        # entreprise_Panneau=el["entreprise_Panneau"]
    # data = {nom_panneau, prenom_panneau,email_Panneau,entreprise_Panneau}
    return render(request, 'pages/Panneaux/creer.html', {
                                                        'edit':edit,
                                                        'id_panneau':id_panneau,
                                                        'nom_panneau':nom_panneau,
                                                        'longitude':longitude,
                                                        'latitude':latitude

                                                        })

def Panneau_delete(request, id):
    link = "http://127.0.0.1:8000/api/panneaus/"+str(id)
    print(link)
    reponse_del_req = requests.delete(link).json()

    reponse = requests.get("http://127.0.0.1:8000/api/panneaus").json()

    messages.success(request, " Panneau supprimé avec succès ")
    return redirect('Panneau_list')

def Panneau_desallouer(request, id):
    link = "http://127.0.0.1:8000/api/panneaus/desallouer/"+str(id)
    reponse_del_req = requests.get(link).json()
    messages.success(request, " Panneau desalloué avec succès ")
    return redirect('Contrat_list')

@csrf_exempt
def Panneau_allouer(request):
    pan=request.GET['id_panneau']
    cont=request.GET['id_contrat']
    url = "http://127.0.0.1:8000/api/panneaus/allouer/element/"+str(pan)+"/"+str(cont)
    a=requests.put(url)
    messages.success(request, " Panneau alloué avec succès ")
    return redirect('Contrat_list')


# contrat --------------------------------------------------------------------------------------

def Contrat_create(request):
    reponse = requests.get("http://127.0.0.1:8000/api/clients").json()
    return render(request, 'pages/Contrats/creer.html',{'data':reponse})

def Contrat_list(request):
    reponse = requests.get("http://127.0.0.1:8000/api/contrats").json()
    tableauDeDate=[]
    for el in reponse:
        debut  = el['dateDebut']
        fin  = el['dateFin']
        debut = datetime.strptime(debut, '%Y-%m-%d')
        fin = datetime.strptime(fin, '%Y-%m-%d')
        r=datetime.now()
        today = r.strftime("%Y-%m-%d")
        # le nombre de jours jusqu'a aujourd'hui
        consommer = r - debut
        # le nombre de joyr total de diffusion
        difference = fin - debut
        el['duree']=difference.days
        el['pourcentage']=(consommer.days*100)/difference.days
        tableauDeDate.append(difference)
    # print(reponse[0]['duree'])
    return render(request, 'pages/Contrats/liste.html',{'data':reponse})

@csrf_exempt
def Contrat_store(request):
    nom_contrat=request.POST['nom_contrat']
    dateDebut=request.POST['dateDebut']
    dateFin=request.POST['dateFin']
    print(request.POST['id_contrat'])
    if request.POST['id_contrat'] =="":
        url ="http://127.0.0.1:8000/api/contrats"
        rep = requests.post(url,data={
            "nom_contrat":request.POST['nom_contrat'],
            "dateDebut":request.POST['dateDebut'],
            "dateFin":request.POST['dateFin'],
            "client_id" :request.POST['client_id']
        }).json()
        print(rep)
        messages.success(request, " Contrat enrégistré avec succès ")
        return redirect('Contrat_create')
    else:
        id = request.POST['id_contrat']
        url ="http://127.0.0.1:8000/api/contrats/"+str(id)
        url = url.replace(" ", "")
        requests.put(url,data={
            "nom_contrat":request.POST['nom_contrat'],
            "dateDebut":request.POST['dateDebut'],
            "dateFin":request.POST['dateFin'],
            "client_id" :request.POST['client_id']
        })
        messages.success(request, " Contrat modifié avec succès ")
        # reponse=requests.get("http://127.0.0.1:8000/api/contrats").json()
        return redirect('Contrat_list')

def Contrat_delete(request, id):
    link = "http://127.0.0.1:8000/api/contrats/"+str(id)
    reponse_del_req = requests.delete(link).json()
    reponse = requests.get("http://127.0.0.1:8000/api/contrats").json()
    messages.success(request, " Contrat supprimé avec succès ")
    return redirect('Contrat_list')

def Contrat_detail(request, id):
    link = "http://127.0.0.1:8000/api/contrats/"+str(id)
    reponse = requests.get(link).json()
    link2 = "http://127.0.0.1:8000/api/panneaus/contrat/"+str(id)
    reponse2 = requests.get(link2).json()
    link3 = "http://127.0.0.1:8000/api/panneaus/libre/free"
    reponse3 = requests.get(link3).json()
    print(reponse2)
    return render(request, 'pages/Contrats/detail.html', {'data':reponse, 'data2': reponse2,'data3': reponse3})

def Contrat_edit(request, id):
    link = "http://127.0.0.1:8000/api/contrats/"+str(id)
    reponse = requests.get(link).json()
    clients = requests.get("http://127.0.0.1:8000/api/clients").json()
    edit=True
    for el in reponse:
        id_contrat=el["id"]
        nom_contrat=el["nom_contrat"]
        prenom_client=el["prenom_client"]
        nom_client=el["nom_client"]
        id_client=el["client_id"]
        dateDebut=el["dateDebut"]
        dateFin=el["dateFin"]
# data = {nom_contrat, dateDebut,dateFin,entreprise_client}
    return render(request, 'pages/Contrats/creer.html', {
                                                        'edit':edit,
                                                        'edit':edit,
                                                        'id_contrat':id_contrat,
                                                        'nom_contrat':nom_contrat,
                                                        'dateDebut':dateDebut,
                                                        'dateFin':dateFin,
                                                        'data':clients,
                                                        'prenom_client':prenom_client,
                                                        'nom_client':nom_client,
                                                        'id_client':id_client
                                                        })

# def contrat_pdf(request):

#     from django.http import HttpResponse
#     from django.views.generic import View

#     from .utils import render_to_pdf #created in step 4

#     class GeneratePdf(View):
#         def get(self, request, *args, **kwargs):
#             data = {
#                 'today': datetime.date.today(),
#                 'amount': 39.99,
#                 'customer_name': 'Cooper Mann',
#                 'order_id': 1233434,
#             }
#             pdf = render_to_pdf('Contrats/contratPdf.html', data)
#             return HttpResponse(pdf, content_type='application/pdf')


from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {

            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pages/Contrats/contratPdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


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