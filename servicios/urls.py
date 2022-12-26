from .api import ServicioViewSet
from rest_framework import routers

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'servicio', ServicioViewSet, 'servicio')
urlpatterns=router.urls