from rest_framework.views import APIView
from rest_framework.response import Response
import os
import requests

class CoinDataView(APIView):

    COINGECKO_API_KEY = os.getenv('COINGECKO')

    def get(self, request, *args, **kwargs):
        coin_list = self.get_coin_list()
        return Response(coin_list)

    def get_coin_list(self, page=1):
        url = "https://pro-api.coingecko.com/api/v3/coins/markets"
        headers = {
            'Accepts': 'application/json', 
            'X-CG-Pro-API-Key': self.COINGECKO_API_KEY
        }
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 100,
            'page': page,
            'sparkline': False   
        }
        response = requests.get(url, headers=headers, params=params)
        coin_data = response.json()
        crypto_list = [self.extract_coin_data(coin) for coin in coin_data]
        return crypto_list

    def extract_coin_data(self, coin):
        return {
            'id': coin['id'],
            'symbol': coin['symbol'],
            'name': coin['name'],
            # Extract the rest of the fields you need...
        }
