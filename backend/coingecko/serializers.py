from rest_framework import serializers
from .models import Coin, HodlCoin, Category

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = "__all__"

class HodlCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = HodlCoin
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"