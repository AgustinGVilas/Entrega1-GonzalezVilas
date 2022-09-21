from socket import fromshare
from django import forms

class formAutomovil(forms.Form):
    
    marca = forms.CharField()
    modelo = forms.CharField()
    año = forms.IntegerField()

class formMotocicleta(forms.Form):
    
    marca = forms.CharField()
    cilindrada = forms.IntegerField()
    año = forms.IntegerField()

class formCamion(forms.Form):
    
    peso = forms.IntegerField()
    capCarga = forms.IntegerField()