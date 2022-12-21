from rest_framework import serializers
from .models import Pagito,Pagito_expirado

class PagitoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pagito
        fields = '__all__'
    
    def validate(self, data):
        monto = data.get('monto')
        if monto<0:
            raise serializers.ValidationError('monto no puede ser negativo')
        return data

class Pagito_expiradoSerializer(serializers.Serializer):
    class Meta:
        model=Pagito_expirado
        fields = '__all__'
        