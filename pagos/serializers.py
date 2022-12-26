from rest_framework import serializers
from .models import Pago, Pago_Expirado


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

    def validate(self,data):
        amount = data.get('monto')
        if amount < 0:
            raise serializers.ValidationError('el valor no puede ser 0')
        return data


class Pago_ExpiradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago_Expirado
        fields = '__all__'