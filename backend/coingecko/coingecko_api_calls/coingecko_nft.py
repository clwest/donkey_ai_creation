import os
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

COINGECKO_API_KEY = os.getenv('COINGECKO')

class NFTCollectionList(APIView):
    def get(self, request, format=None):
        url = 'https://pro-api.coingecko.com/api/v3/nfts/list'
        headers = {
            'Accepts': 'application/json',
            'X-CG-Pro-API-Key': COINGECKO_API_KEY,
        }

        response = requests.get(url, headers=headers)
        nft_data = response.json()

        nft_list = []
        for nft in nft_data:
            nft_list.append({
                'id': nft['id'],
                'contractAddress': nft['contract_address'],
                'name': nft['name'],
                'assetPlatformId': nft['asset_platform_id'],
                'symbol': nft['symbol'],
            })

        return Response(nft_list)

class NFTCollectionById(APIView):
    def get(self, request, id, format=None):
        nft_url = f'https://pro-api.coingecko.com/api/v3/nfts/{id}'
        market_chart_url = f'https://pro-api.coingecko.com/api/v3/nfts/{id}/market_chart'

        headers = {
            'Accepts': 'application/json',
            'X-CG-Pro-API-Key': COINGECKO_API_KEY,
        }

        params = {'localization': 'false'}
        market_chart_params = {'vs_currency': 'usd', 'days': '30'}

        nft_response = requests.get(nft_url, headers=headers, params=params)
        market_chart_response = requests.get(market_chart_url, headers=headers, params=market_chart_params)

        nft_data = nft_response.json()
        market_chart_data = market_chart_response.json()

        nft_collection = {
            'id': nft_data['id'],
            'contractAddress': nft_data['contract_address'],
            'assetPlatformId': nft_data['asset_platform_id'],
            'name': nft_data['name'],
            'symbol': nft_data['symbol'],
            'image': nft_data['image']['small'],
            'description': nft_data['description'],
            'links': {
                'homepage': nft_data['links'].get('homepage', []),
                'twitter': nft_data['links'].get('twitter', ""),
                'discord': nft_data['links'].get('discord', ""),
            },
            'nativeCurrency': nft_data['native_currency'],
            'floorPrice': {
                'nativeCurrency': nft_data['floor_price']['native_currency'],
                'usd': nft_data['floor_price']['usd'],
            },
            'marketCap': {
                'nativeCurrency': nft_data['market_cap']['native_currency'],
                'usd': nft_data['market_cap']['usd'],
            },
            'volume24H': {
                'nativeCurrency': nft_data['volume_24h']['native_currency'],
                'usd': nft_data['volume_24h']['usd'],
            },
            'floorPriceInUsd': nft_data['floor_price_in_usd_24h_percentage_change'],
            'numberOfUniqueAddresses': nft_data['number_of_unique_addresses'],
            'numberOfAddressesChanged24h': nft_data['number_of_unique_addresses_24h_percentage_change'],
            'totalSupply': nft_data['total_supply'],
            'marketChart': market_chart_data,
        }

        return Response(nft_collection)

class NFTCollectionMarket(APIView):
    def get(self, request, format=None):
        url = 'https://pro-api.coingecko.com/api/v3/nfts/markets'
        headers = {
            'Accepts': 'application/json',
            'X-CG-Pro-API-Key': COINGECKO_API_KEY,
        }

        response = requests.get(url, headers=headers)
        nft_data = response.json()

        nft_market = []
        for nft in nft_data:
            nft_market.append({
                'id': nft['id'],
                'contractAddress': nft['contract_address'],
                'name': nft['name'],
                'symbol': nft['symbol'],
                'image': nft['image']['small'],
                'description': nft['description'],
                'nativeCurrency': nft['native_currency'],
                'floorPrice': {
                    'nativeCurrency': nft['floor_price']['native_currency'],
                    'usd': nft['floor_price']['usd'],
                },
                'marketCap': {
                    'nativeCurrency': nft['market_cap']['native_currency'],
                    'usd': nft['market_cap']['usd'],
                },
                'volume24H': {
                    'nativeCurrency': nft['volume_24h']['native_currency'],
                    'usd': nft['volume_24h']['usd'],
                },
                'floorPriceChangedInUsd24': nft['floor_price_in_usd_24h_percentage_change'],
                'numberOfUniqueAddresses': nft['number_of_unique_addresses'],
                'numberOfAddressesChanged24h': nft['number_of_unique_addresses_24h_percentage_change'],
                'totalSupply': nft['total_supply'],
            })

        return Response(nft_market)


