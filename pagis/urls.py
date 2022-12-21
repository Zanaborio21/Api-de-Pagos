from . import api
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'pegis',api.PagitoView,'pagitos')
router.register(r'pegis',api.Pagito_expiradoView,'pagitos')

urlpatterns = router.urls

