from rest_framework import serializers
from .models import Servis

class ServisSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servis
        fields = '__all__'
        read_only_fields = '__all__',