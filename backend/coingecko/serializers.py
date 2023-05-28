from rest_framework import serializers
from .models import Coin, HodlCoin

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = "__all__"

class HodlCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = HodlCoin
        fields = "__all__"