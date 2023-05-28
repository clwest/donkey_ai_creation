from rest_framework.views import APIView
from rest_framework.response import Response
import os
import requests

class DerivativesView(APIView):

    COINGECKO_API_KEY = os.getenv('COINGECKO')

    def get(self, request, *args, **kwargs):
        derivatives = self.get_derivatives()
        return Response(derivatives)

    def get_derivatives(self):
        url = "https://pro-api.coingecko.com/api/v3/derivatives"
        headers = {
            'Accepts': 'application/json', 
            'X-CG-Pro-API-Key': self.COINGECKO_API_KEY
        }
        response = requests.get(url, headers=headers)
        derivative_data = response.json()
        derivatives = [self.extract_derivative_data(data) for data in derivative_data]
        return derivatives

    def extract_derivative_data(self, data):
        return {
            'market': data['market'],
            'symbol': data['symbol'],
            'indexId': data['index_id'],
            'price': data['price'],
            'pricePercentageChange24h': data['price_percentage_change_24h'],
            'contractType': data['contract_type'],
            'index': data['index'],
            'basis': data['basis'],
            'spread': data['spread'],
            'fundingRate': data['funding_rate'],
            'openInterest': data['open_interest'],
            'volume24h': data['volume_24h'],
            'lastTradedAt': data['last_traded_at'],
            'expiredAt': data['expired_at'],
        }

class DerivativeExchangesView(APIView):

    COINGECKO_API_KEY = os.getenv('COINGECKO')

    def get(self, request, *args, **kwargs):
        derivative_exchanges = self.get_derivative_exchanges()
        return Response(derivative_exchanges)

    def get_derivative_exchanges(self):
        url = "https://pro-api.coingecko.com/api/v3/derivatives/exchanges"
        headers = {
            'Accepts': 'application/json', 
            'X-CG-Pro-API-Key': self.COINGECKO_API_KEY
        }
        response = requests.get(url, headers=headers)
        derivative_exchanges_data = response.json()
        derivative_exchanges = [self.extract_derivative_exchange_data(data) for data in derivative_exchanges_data]
        return derivative_exchanges

    def extract_derivative_exchange_data(self, data):
        return {
            'name': data['name'],
            'id': data['id'],
            'openInterestBtc': data['open_interest_btc'],
            'tradeVolume24hBTC': data['trade_volume_24h_btc'],
            'numberOfPerpetualPairs': data['number_of_perpetual_pairs'],
            'numberOfFuturesPairs': data['number_of_futures_pairs'],
            'image': data['image'],
            'yearEstablished': data['year_established'],
            'country': data['country'],
            'description': data['description'],
            'url': data['url']
        }

class DerivativeExchangeByIdView(APIView):

    COINGECKO_API_KEY = os.getenv('COINGECKO')

    def get(self, request, id, *args, **kwargs):
        derivative_exchange = self.get_derivative_exchange_by_id(id)
        return Response(derivative_exchange)

    def get_derivative_exchange_by_id(self, id):
        url = f"https://pro-api.coingecko.com/api/v3/derivatives/exchanges/{id}"
        headers = {
            'Accepts': 'application/json', 
            'X-CG-Pro-API-Key': self.COINGECKO_API_KEY
        }
        params = {'localization': 'false'}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        derivative_exchange_id = {
            'name': data['name'],
            'openInterestBTC': data['open_interest_btc'],
            'tradeVolume24hBTC': data['trade_volume_24h_btc'],
            'numberOfPerpetualPairs': data['number_of_perpetual_pairs'],
            'numberOfFuturesPairs': data['number_of_futures_pairs'],
            'image': data['image'],
            'yearEstablished': data['year_established'],
            'country': data['country'],
            'description': data['description'],
            'url': data['url'],
        }
        return derivative_exchange_id

