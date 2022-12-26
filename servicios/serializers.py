from rest_framework import serializers
from.models import Service

class ServicioSerializer(serializers.ModelSerializer):
        class Meta:
            model=Service
            fields = '__all__'
            #read_only_fields = '__all__',
