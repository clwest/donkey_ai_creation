from rest_framework import routers
from django.urls import path
from .views import CoinViewSet, HodlCoinViewSet 

router = routers.DefaultRouter()
router.register(r'coins', CoinViewSet, basename='list')
router.register(r'hodl-coins', HodlCoinViewSet, basename='hodl_coin_list')


urlpatterns = [
    path('list/', CoinViewSet.as_view({'get': 'list'}), name='coin-list')
]



