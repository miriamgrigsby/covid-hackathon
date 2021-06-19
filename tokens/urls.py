from rest_framework import routers
from .api import TokensViewSet

router = routers.DefaultRouter()
router.register('api/tokens', TokensViewSet, 'tokens')


urlpatterns = router.urls