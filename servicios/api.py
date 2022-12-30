from .models import Service
from rest_framework import viewsets,permissions
from .serializers import ServicioSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


class ServicioViewSet(viewsets.ModelViewSet):
    queryset=Service.objects.get_queryset().order_by('id')
    serializer_class=ServicioSerializer
  
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return[IsAdminUser()]