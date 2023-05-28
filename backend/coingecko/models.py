from django.conf import settings
from django.db import models

class Coin(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    image = models.URLField(null=True, blank=True)
    current_price = models.FloatField(null=True, blank=True)
    market_cap = models.FloatField(null=True, blank=True)
    market_cap_rank = models.IntegerField(null=True, blank=True)
    total_volume = models.FloatField(null=True, blank=True)
    high_24h = models.FloatField(null=True, blank=True)
    low_24h = models.FloatField(null=True, blank=True)
    price_change_24h = models.FloatField(null=True, blank=True)
    price_change_percentage_24h = models.FloatField(null=True, blank=True)
    market_cap_change_24h = models.FloatField(null=True, blank=True)
    market_cap_change_percentage_24h = models.FloatField(null=True, blank=True)
    circulating_supply = models.FloatField(null=True, blank=True)
    total_supply = models.FloatField(null=True, blank=True)
    ath = models.FloatField(null=True)
    ath_change_percentage = models.FloatField(null=True)
    ath_date = models.DateTimeField(null=True)
    atl = models.FloatField(null=True)
    atl_change_percentage = models.FloatField(null=True)
    atl_date = models.DateTimeField(null=True)
    last_updated = models.DateTimeField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
    
    
    """create models for the Coingecko API calls here"""
class HodlCoin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name + " " + self.coin.name