from django.contrib import admin
from .models import Pago,Pago_Expirado

# Register your models here.


admin.site.register(Pago)
admin.site.register(Pago_Expirado)