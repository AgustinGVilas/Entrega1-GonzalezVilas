from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('automovil/', automovil, name="Automovil"),
    path('motocicleta/', motocicleta, name="Motocicleta"),
    path('camion/', camion, name="Camion"),
    
    path('busquedavehiculo/', busquedaVehiculo, name="BusquedaVehiculo"),
    path('busqueda1', busqueda1, name='busqueda1'),
    path('busqueda2', busqueda2, name='busqueda2'),
    path('busqueda3', busqueda3, name='busqueda3'),
    
    path('busquedaAutos/', busquedaAutos),
    path('busquedaMotos/', busquedaMotos),
    path('busquedaCamiones/', busquedaCamiones),
    
]