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
