from rest_framework import routers
from django.urls import path
from .views import CoinViewSet, HodlCoinViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'coins', CoinViewSet, basename='list')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'hodl-coins', HodlCoinViewSet, basename='hodl_coin_list')


urlpatterns = [
    path('list/', CoinViewSet.as_view({'get': 'list'}), name='coin-list'),
    path('category/', CategoryViewSet.as_view({'get': 'list'}), name='category-list')
]



