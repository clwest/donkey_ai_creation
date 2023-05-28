import os
import requests
from dotenv import load_dotenv
load_dotenv()

COINGECKO_API_KEY = os.getenv('COINGECKO')

def get_coin_list():
    url = f"https://pro-api.coingecko.com/api/v3/coins/markets"
    headers = {
            'Accepts': 'application/json', 
            'X-CG-Pro-API-Key': COINGECKO_API_KEY
        }
    params = {
            'vs_currency': 'usd',
        }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if not data:
        return
    coin_list = []
    for coin in data:
        coin_dict = {
            'id': coin['id'],
            'symbol': coin['symbol'],
            'name': coin['name'],
            'image': coin['image'],
            'current_price': coin['current_price'],
            'market_cap': coin['market_cap'],
            'market_cap_rank': coin['market_cap_rank'],
            'fully_diluted_valuation': coin['fully_diluted_valuation'],
            'total_volume': coin['total_volume'],
            'high_24h': coin['high_24h'],
            'low_24h': coin['low_24h'],
            'price_change_24h': coin['price_change_24h'],
            'price_change_percentage_24h': coin['price_change_percentage_24h'],
            'market_cap_change_24h': coin['market_cap_change_24h'],
            'market_cap_change_percentage_24h': coin['market_cap_change_percentage_24h'],
            'circulating_supply': coin['circulating_supply'],
            'total_supply': coin['total_supply'],
            'max_supply': coin['max_supply'],
            'ath': coin['ath'],
            'ath_change_percentage': coin['ath_change_percentage'],
            'ath_date': coin['ath_date'],
            'atl': coin['atl'],
            'atl_change_percentage': coin['atl_change_percentage'],
            'atl_date': coin['atl_date'],
            'roi': coin['roi'],
            'last_updated': coin['last_updated'],    
        }
        coin_list.append(coin_dict)
    return coin_list



def get_categories():
    url = f"https://pro-api.coingecko.com/api/v3/coins/categories"
    headers = {
            'Accepts': 'application/json',
            'X-CG-Pro-API-Key': COINGECKO_API_KEY
        }
    response = requests.get(url, headers=headers)
    category_data = response.json()
    if not category_data:
        return
    categories = []
    for category in category_data:
        category_dict = {
            'id': category['id'],
            'name': category['name'],
            'market_cap': category['market_cap'],
            'market_cap_change_24h': category['market_cap_change_24h'],
            'content': category['content'],
            'top_3_coins': category['top_3_coins'],
            'volume_24h': category['volume_24h'],
            'updated_at': category['updated_at']
        }
        categories.append(category_dict)
    return categories


def get_category_list():
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

        return category_list