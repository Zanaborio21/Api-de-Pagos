from django.db import models
from users.models import User
from servis.models import Servis

# Create your models here.

class Pagito(models.Model):
    usuario=models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuarito')
    servicio=models.ForeignKey(Servis,on_delete=models.CASCADE,related_name='servis')
    monto=models.FloatField(default=0.0)
    fecha_pago=models.DateField()
    fecha_expiracion=models.DateField()

    def __str__(self) -> str:
        return self.usuario , self.servicio

class Pagito_expirado(models.Model):
    pagito_id=models.ForeignKey(Pagito, on_delete=models.CASCADE)
    fee=models.DecimalField(max_digits=10, decimal_places=2)


