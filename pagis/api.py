from .models import Pagito_expirado,Pagito
from rest_framework import viewsets
from .serializers import PagitoSerializer,Pagito_expiradoSerializer
from rest_framework import viewsets,filters
from rest_framework import permissions

class PagitoView(viewsets.ModelViewSet):
    queryset=Pagito.objects.get_queryset().order_by('id')
    serializer_class=PagitoSerializer
    permission_classes=[permissions.AllowAny]

class Pagito_expiradoView(viewsets.ModelViewSet):
    queryset=Pagito_expirado.objects.get_queryset().order_by('id')
    serializer_class=Pagito_expiradoSerializer
    permission_classes=[permissions.AllowAny]
