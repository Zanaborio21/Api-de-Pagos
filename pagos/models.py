from django.db import models

from users.models import User
from servicios.models import Service

# Create your models here.

class Pago(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()
    fecha_expiracion = models.DateField()



class Pago_Expirado(models.Model):
    pago_id = models.ForeignKey(Pago, on_delete=models.CASCADE)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
