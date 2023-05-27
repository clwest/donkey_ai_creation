from django.urls import path, include
from rest_framework import routers
from .views import CryptoNewsViewSet, AllTickersViewSet, TrendingViewSet, EventViewSet, TopMentionCryptoViewSet, CryptoNewsSourceViewSet

router = routers.DefaultRouter()
router.register(r'news', CryptoNewsViewSet, basename='news')
router.register(r'source', CryptoNewsSourceViewSet, basename='source')
router.register(r'all-tickers', AllTickersViewSet, basename='all-tickers')
router.register(r'trending', TrendingViewSet, basename='trending')
router.register(r'events', EventViewSet, basename='events')
router.register(r'top-mentions', TopMentionCryptoViewSet, basename='top-mentions')

urlpatterns = [
    path('news/', CryptoNewsViewSet.as_view({'get': 'list'}), name='news-list'),
    path('sources/', CryptoNewsSourceViewSet.as_view({'get': 'list'}), name='news-source-list'),
    path('sources/<str:name>/', CryptoNewsSourceViewSet.as_view({'get': 'retrieve'}), name='news-source-detail'),
    path('alltickers/', AllTickersViewSet.as_view({'get': 'list'}), name='alltickers-list'),
    path('trending/', TrendingViewSet.as_view({'get': 'list'}), name='trending-list'),
    path('trending/<str:ticker>/', TrendingViewSet.as_view({'get': 'retrieve'}), name='trending-detail'),
    path('events/', EventViewSet.as_view({'get': 'list'}), name='events-list'),
    path('events/<int:event_id>/', EventViewSet.as_view({'get': 'retrieve'}), name='events-detail'),
    path('top-mentioned/', TopMentionCryptoViewSet.as_view({'get': 'list'}), name='top-mentioned-list'),
]
