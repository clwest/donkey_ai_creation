from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Coin, HodlCoin
from .serializers import CoinSerializer, HodlCoinSerializer
from .coingecko_coins import get_coin_list
from dotenv import load_dotenv
import os   
load_dotenv()





class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


    def list(self, request, *args, **kwargs):
        data = get_coin_list()
        serializer = CoinSerializer(data=data, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def create(self, request, *args, **kwargs):
        data = get_coin_list()
        serializer = CoinSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class HodlCoinViewSet(viewsets.ModelViewSet):
    queryset = HodlCoin.objects.all()
    serializer_class = HodlCoinSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)