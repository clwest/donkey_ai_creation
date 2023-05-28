import os
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

COINGECKO_API_KEY = os.getenv('COINGECKO')


class MarketOpenHighLowClose(APIView):
    def get(self, request, id, days='7', format=None):
        url = f'https://pro-api.coingecko.com/api/v3/coins/{id}/ohlc'
        params = {
            'id': id,
            'vs_currency': 'usd',
            'days': days,
        }
        headers = {
            'Accepts': 'application/json',
            'X-CG-Pro-API-Key': COINGECKO_API_KEY,
        }
        response = requests.get(url, headers=headers, params=params)
        market_ohlc = response.json()

        return Response(market_ohlc)


class CoinHistoricalData(APIView):
    def get(self, request, id, days='30', interval='daily', format=None):
        url = f'https://pro-api.coingecko.com/api/v3/coins/{id}/market_chart'
        params = {
            'vs_currency': 'usd',
            'days': days,
            'interval': interval,
        }
        headers = {
            'Accepts': 'application/json',
            'X-CG-Pro-API-Key': COINGECKO_API_KEY,
        }
        response = requests.get(url, headers=headers, params=params)
        historical_data = response.json()

        return Response(historical_data)


class MarketChartRange(APIView):
    def get(self, request, id, vs_currency='usd', from_time, to_time, format=None):
        url = f'https://pro-api.coingecko.com/api/v3/coins/{id}/market_chart/range'
        params = {
            'vs_currency': vs_currency,
            'from': from_time,
            'to': to_time,
        }
        headers = {
            'Accepts': 'application/json',
            'X-CG-Pro-API-Key': COINGECKO_API_KEY,
        }
        response = requests.get(url, headers=headers, params=params)
        market_chart_data = response.json()

        return Response(market_chart_data)
