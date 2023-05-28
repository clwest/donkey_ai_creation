import requests
import os
from rest_framework.views import APIView
from rest_framework.response import Response

COINGECKO_API_KEY = os.environ.get('COINGECKO')

class CategoriesView(APIView):
    def get(self, request, format=None):
        url = "https://pro-api.coingecko.com/api/v3/coins/categories"
        headers = {
            'Accepts': 'application/json',
            'X-CG-Pro-API-Key': COINGECKO_API_KEY
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        category_data = response.json()

        categories = list(map(lambda data: {
            'id': data['id'],
            'name': data['name'],
            'marketCap': data['market_cap'],
            'marketCapChange24h': data['market_cap_change_24h'],
            'content': data['content'],
            'top3Coins': data['top_3_coins'],
            'volume24h': data['volume_24h'],
            'updatedAt': data['updated_at']
        }, category_data))

        return Response(categories)


class CategoryListView(APIView):
    def get(self, request, format=None):
        url = "https://pro-api.coingecko.com/api/v3/coins/categories"
        headers = {
            'Accepts': 'application/json',
            'X-CG-Pro-API-Key': COINGECKO_API_KEY
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        category_list_data = response.json()

        category_list = list(map(lambda data: {
            'categoryId': data['category_id'],
            'name': data['name'],
        }, category_list_data))

        return Response(category_list)
