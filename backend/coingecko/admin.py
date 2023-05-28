
from django.contrib import admin
from .models import Coin, HodlCoin

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'symbol', 'current_price', 'market_cap', 'market_cap_rank']
    search_fields = ['id', 'name', 'symbol']

@admin.register(HodlCoin)
class HodlCoinAdmin(admin.ModelAdmin):
    list_display = ['user', 'coin']
    search_fields = ['user__username', 'coin__name']
