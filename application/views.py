from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Client_create(request):
    return render(request, 'pages/Clients/creer.html')

def Client_list(request):
    return render(request, 'pages/Clients/liste.html')

def Contrat_create(request):
    return render(request, 'pages/Contrats/creer.html')

def Contrat_list(request):
    return render(request, 'pages/Contrats/liste.html')