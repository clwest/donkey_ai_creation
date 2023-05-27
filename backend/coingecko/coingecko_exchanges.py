from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os

class ExchangeList(APIView):
    COINGECKO_API_KEY = os.getenv('COINGECKO')

    def get(self, request, format=None):
        url = "https://pro-api.coingecko.com/api/v3/exchanges"
        headers = {
            'Accepts': 'application/json', 
            'X-CG-Pro-API-Key': self.COINGECKO_API_KEY
        }
        response = requests.get(url, headers=headers)
        exchange_data = response.json()

        exchanges = [
            {
                'id': data['id'],
                'name': data['name'],
                'yearEstablished': data['year_established'],
                'country': data['country'],
                'description': data['description'],
                'url': data['url'],
                'image': data['image'],
                'hasTradeIncentive': data['has_trade_incentive'],
                'trustScore': data['trust_score'],
                'trustScoreRank': data['trust_score_rank'],
                'tradeVolume24hBTC': data['trade_volume_24h_btc'],
                'tradeVolume24hBTCNormalized': data['trade_volume_24h_btc_normalized']
            } for data in exchange_data
        ]

        return Response(exchanges)


class ExchangeDetail(APIView):
    COINGECKO_API_KEY = os.getenv('COINGECKO')

    def get(self, request, id, format=None):
        url = f"https://pro-api.coingecko.com/api/v3/exchanges/{id}"
        headers = {
            'Accepts': 'application/json', 
            'X-CG-Pro-API-Key': self.COINGECKO_API_KEY
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        exchange_details = {
            'id': data['id'],
            'name': data['name'],
            'yearEstablished': data['year_established'],
            'country': data['country'],
            'description': data['description'],
            'url': data['url'],
            'image': data['image'],
            'facebookUrl': data['facebook_url'],
            'redditUrl': data['reddit_url'],
            'telegramUrl': data['telegram_url'],
            'slackUrl': data['slack_url'],
            'otherUrl1': data['other_url_1'],
            'otherUrl2': data['other_url_2'],
            'twitterScreenName': data['twitter_screen_name'],
            'trustScore': data['trust_score'],
            'trustScoreRank': data['trust_score_rank'],
            'tradeVolume24hBTC': data['trade_volume_24h_btc'],
            'tradeVolume24hBTCNormalized': data['trade_volume_24h_btc_normalized'],
        }

        return Response(exchange_details)

class ExchangeTickers(APIView):
    COINGECKO_API_KEY = os.getenv('COINGECKO')

    def get(self, request, id, page=1, per_page=100, format=None):
        url = f"https://pro-api.coingecko.com/api/v3/exchanges/{id}/tickers"
        headers = {
            'Accepts': 'application/json', 
            'X-CG-Pro-API-Key': self.COINGECKO_API_KEY
        }
        params = {
            'page': page,
            'per_page': per_page,
        }
        response = requests.get(url, headers=headers, params=params)
        tickers_data = response.json()['tickers']
        tickers = [
            {
                'base': ticker['base'],
                'target': ticker['target'],
                'market': ticker['market'],
                'last': ticker['last'],
                'volume': ticker['volume'],
                'converted_last': ticker['converted_last'],
                'trade_url': ticker['trade_url'],
                'trust_score': ticker['trust_score'],
                'bid_ask_spread_percentage': ticker['bid_ask_spread_percentage'],
                'timestamp': ticker['timestamp'],
                'last_traded_at': ticker['last_traded_at'],
                'last_fetch_at': ticker['last_fetch_at'],
                'is_anomaly': ticker['is_anomaly'],
                'is_stale': ticker['is_stale'],
                'trade_url': ticker['trade_url'],
                'token_info_url': ticker['token_info_url'],
                'coin_id': ticker['coin_id'],
                'target_coin_id': ticker['target_coin_id'],
            } for ticker in tickers_data
        ]

        return Response(tickers)

