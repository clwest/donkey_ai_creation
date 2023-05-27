from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import CoinViewSet

router = SimpleRouter()
router.register('coins', CoinViewSet, basename='coin')

urlpatterns = router.urls
