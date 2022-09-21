from django.contrib import admin
from .models import *


# Register your models here.

#user: agustingv
#a@b.com
#pass 12345

admin.site.register(Automovil)
admin.site.register(Motocicleta)
admin.site.register(Camion)