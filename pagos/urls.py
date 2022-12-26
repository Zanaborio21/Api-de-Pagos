from .api import Pago_ExpiradoView,PagoView
from rest_framework import routers

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pago', PagoView, 'pago')
router.register(r'pago_expirado', Pago_ExpiradoView, 'pago_expirado')
urlpatterns=router.urls