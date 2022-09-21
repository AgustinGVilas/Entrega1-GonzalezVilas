from django.shortcuts import render
from django.http import HttpResponse

from .forms import formAutomovil, formCamion, formMotocicleta
from .models import Automovil, Camion, Motocicleta

# Create your views here.

def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def automovil(request):

    if request.method == 'POST':

        miFormu = formAutomovil(request.POST)

        if miFormu.is_valid():

            info = miFormu.cleaned_data

            automovil = Automovil (marca = info['marca'], modelo = info['modelo'], año = info['año'])

            automovil.save()

            return render(request, 'AppCoder/inicio.html')


    else:

        miFormu = formAutomovil()            

    return render(request, 'AppCoder/automovil.html', {"miFormu": miFormu})



def motocicleta(request):

    if request.method == 'POST':

        miFormu = formMotocicleta(request.POST)

        if miFormu.is_valid():

            info = miFormu.cleaned_data

            moto = Motocicleta (marca = info['marca'], cilindrada = info['cilindrada'], año = info['año'])

            moto.save()

            return render(request, 'AppCoder/inicio.html')


    else:

        miFormu = formMotocicleta()            

    return render(request, 'AppCoder/motocicleta.html', {"miFormu": miFormu})



def camion(request):

    if request.method == 'POST':

        miFormu = formCamion(request.POST)

        if miFormu.is_valid():

            info = miFormu.cleaned_data

            camion = Camion (peso = info['peso'], capCarga = info['capCarga'])

            camion.save()

            return render(request, 'AppCoder/inicio.html')


    else:

        miFormu = formCamion()            

    return render(request, 'AppCoder/camion.html', {"miFormu": miFormu})




def busquedaVehiculo(request):
    
    return render (request, 'AppCoder/busquedavehiculos.html')



def busqueda1(request):

    return render(request, 'AppCoder/busquedaAutos.html')

def busqueda2(request):

    return render(request, 'AppCoder/busquedaMotos.html')

def busqueda3(request):

    return render(request, 'AppCoder/busquedaCamiones.html')



def busquedaAutos(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]

        auto = Automovil.objects.filter(marca__icontains=marca)

        return render(request, 'AppCoder/busquedaDeAutos.html', {"auto":auto, "marca": marca})

    else:
        mensaje = "No enviaste datos"

    return HttpResponse(mensaje)


def busquedaMotos(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]

        moto = Motocicleta.objects.filter(marca__icontains=marca)

        return render(request, 'AppCoder/busquedaDeMotos.html', {"moto":moto, "marca": marca})

    else:
        mensaje = "No enviaste datos"

    return HttpResponse(mensaje)



def busquedaCamiones(request):

    if request.GET["peso"]:

        peso = request.GET["peso"]

        camion = Camion.objects.filter(peso__icontains=peso)

        return render(request, 'AppCoder/busquedaDeCamiones.html', {"camion":camion, "peso": peso})

    else:
        mensaje = "No enviaste datos"

    return HttpResponse(mensaje)






