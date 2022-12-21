from .models import Servis
from rest_framework import viewsets
from.serializers import ServisSerializer
from rest_framework import permissions
from rest_framework import viewsets,filters

class ServisViewSet(viewsets.ModelViewSet):
    queryset=Servis.objects.get_queryset().order_by('id')
    serializer_class=ServisSerializer
    permission_classes=[permissions.AllowAny]
