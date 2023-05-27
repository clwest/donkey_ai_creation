from rest_framework import viewsets
from .models import Coin
from .serializers import CoinSerializer

class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
