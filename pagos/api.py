from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework import status

from .models import Pago, Pago_Expirado
from .serializers import PagoSerializer, Pago_ExpiradoSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from rest_framework import viewsets




class PagoView(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        return [IsAdminUser()]


    def create(self, request):        
        serializer = PagoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            payment_date = serializer.data.get('fecha_pago')
            expiration_date = serializer.data.get('fecha_expiracion')
            if expiration_date<payment_date:
                record = {
                    "fee": 0.2*float(serializer.data.get('monto')),
                    "pago_id":serializer.data.get('id')
                }
                serializer2 = Pago_ExpiradoSerializer(data=record)
                if serializer2.is_valid():
                    serializer2.save()
                    return Response({
                        "ok":True,
                        "message":"Pago agregado",
                        "data 1":serializer.data,
                        "message":"Pago agregado , pero con retraso",
                        "data 2":serializer2.data
                    }, status=status.HTTP_201_CREATED)

            return Response({
                "ok":True,
                "message":"Pago agregado",
                "data":serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "ok":False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class Pago_ExpiradoView(viewsets.ModelViewSet):
    queryset = Pago_Expirado.objects.all()
    serializer_class = Pago_ExpiradoSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        return [IsAdminUser()]