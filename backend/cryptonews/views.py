from django.shortcuts import render
# views.py
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import CryptoNewsSerializer, CryptoNewsSourceSerializer, TrendingSerializer, EventSerializer, TopMentionsSerializer, AllTickersNewsSerializer
from .crypto_news import get_crypto_news, all_ticker_news, get_trending_headlines,  get_event_articles, get_top_mentioned_crypto_tickers

class CryptoNewsViewSet(viewsets.ViewSet):
    def list(self, request):
        data = get_crypto_news()
        serializer = CryptoNewsSerializer(data=data, many=True)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class CryptoNewsSourceViewSet(viewsets.ViewSet):
    def list(self, request):
        sources = [
          {"name": "AMBCrypto", "value": "AMBCrypto"},
          {"name": "BeInCrypto", "value": "BeInCrypto"},
          {"name": "Benzinga", "value": "Benzinga"},
          {"name": "Bitcoin.com", "value": "Bitcoin"},
          {"name": "Bitcoin Magazine", "value": "Bitcoin+Magazine"},
          {"name": "Bitcoinist", "value": "Bitcoinist"},
          {"name": "Bit News", "value": "Bit+News"},
          {"name": "Bitcoinworld", "value": "Bitcoinworld"},
          {"name": "Blockchain News", "value": "Blockchain+News"},
          {"name": "BlockchainReporter", "value": "BlockchainReporter"},
          {"name": "Blockgeeks", "value": "Blockgeeks"},
          {"name": "Blockonomi", "value": "Blockonomi"},
          {"name": "Blockworks", "value": "Blockworks"},
          {"name": "Bloomberg Markets and Finance (video)", "value": "Bloomberg+Markets+and+Finance"},
          {"name": "Bloomberg Technology", "value": "Bloomberg+Technology"},
          {"name": "Business Insider", "value": "Business+Insider"},
          {"name": "CNBC", "value": "CNBC"},
          {"name": "CNBC Television", "value": "CNBC+Television"},
          {"name": "CNN", "value": "CNN"},
          {"name": "Coinbureau", "value": "Coinbureau"},
          {"name": "Coindesk", "value": "Coindesk"},
          {"name": "Coindoo", "value": "Coindoo"},
          {"name": "Coinfomania", "value": "Coinfomania"},
          {"name": "Coingape", "value": "Coingape"},
          {"name": "Coin Idol", "value": "Coin+Idol"},
          {"name": "Coincu", "value": "Coincu"},
          {"name": "CoinMarketCap", "value": "CoinMarketCap"},
          {"name": "Coinnounce", "value": "Coinnounce"},
          {"name": "Coinspeaker", "value": "Coinspeaker"},
          {"name": "CrowdFundInsider", "value": "CrowdFundInsider"},
          {"name": "Crypto Briefing", "value": "Crypto+Briefing"},
          {"name": "Crypto Daily", "value": "Crypto+Daily"},
          {"name": "Crypto Economy", "value": "Crypto+Economy"},
          {"name": "Cryptoknowmics", "value": "Cryptoknowmics"},
          {"name": "CryptoNews", "value": "CryptoNews"},
          {"name": "Crypto News Flash", "value": "CryptoNewsFlash"},
          {"name": "Crypto.news", "value": "Crypto+News"},
          {"name": "CryptoNinjas", "value": "CryptoNinjas"},
          {"name": "Cryptopolitan", "value": "Cryptopolitan"},
          {"name": "CryptoPotato", "value": "CryptoPotato"},
          {"name": "Crypto Reporter", "value": "Crypto+Reporter"},
          {"name": "CryptoSlate", "value": "CryptoSlate"},
          {"name": "CryptoTicker", "value": "CryptoTicker"},
          {"name": "Cryptoverze", "value": "Cryptoverze"},
          {"name": "DailyCoin", "value": "Dailycoin"},
          {"name": "Daily FX", "value": "DailyFX"},
          {"name": "DC Forecasts", "value": "DCForecasts"},
          {"name": "Decrypt", "value": "Decrypt"},
          {"name": "Ethereum World News", "value": "EWN"},
          {"name": "FinanceMagnates", "value": "FinanceMagnates"},
          {"name": "Finbold", "value": "Finbold"},       
          {"name": "Forbes", "value": "Forbes"},
          {"name": "Fox Business", "value": "Fox+Business"},
          {"name": "FX Empire", "value": "FxEmpire"},
          {"name": "Inside Bitcoins", "value": "Inside+Bitcoins"},
          {"name": "InvestingCube", "value": "InvestingCube"},
          {"name": "Investorplace", "value": "Investorplace"},
          {"name": "Koinpost", "value": "Koinpost"},
          {"name": "Live Bitcoin News", "value": "LiveBitcoinNews"},
          {"name": "Modern Consensus", "value": "Modern+Consensus"},
          {"name": "NewsBTC", "value": "NewsBTC"},
          {"name": "Reuters", "value": "Reuters"},
          {"name": "The Block", "value": "The+Block"},
          {"name": "The Crypto Updates", "value": "TCU"},
          {"name": "The Cryptonomist", "value": "The+Cryptonomist"},
          {"name": "The Currency Analytics", "value": "The+Currency+Analytics"},
          {"name": "The Daily Hodl", "value": "The+Daily+Hodl"},
          {"name": "The Motley Fool", "value": "The+Motley+Fool"},
          {"name": "The News Crypto", "value": "TheNewsCrypto"},
          {"name": "Tokenpost", "value": "Tokenpost"},
          {"name": "Trustnode", "value": "Trustnodes"},
          {"name": "UToday", "value": "UToday"},
          {"name": "Vauld", "value": "Vauld"},
          {"name": "Yahoo Finance (video)", "value": "Yahoo+Finance"},
          {"name": "Zycrypto", "value": "Zycrypto"},
          {"name": "8BTC", "value": "8BTC"},
        ]

        serializer = CryptoNewsSourceSerializer(sources, many=True)
        return Response(serializer.data)

class AllTickersViewSet(viewsets.ViewSet):
  def list(self, request):
    news = all_ticker_news()
    serializer = AllTickersNewsSerializer(news, many=True)
    return Response(serializer.data)

class TrendingViewSet(viewsets.ViewSet):
    def list(self, request):
        ticker = request.GET.get('ticker', None)
        trending = get_trending_headlines(ticker=ticker)
        serializer = TrendingSerializer(trending, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EventViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = get_event_articles()
        serializer = EventSerializer(articles, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        articles = get_event_articles(tickers=pk)
        serializer = EventSerializer(articles, many=True)
        return Response(serializer.data)



class TopMentionCryptoViewSet(viewsets.ViewSet):
  def list(self, request):
    top_mentioned = get_top_mentioned_crypto_tickers()
    serializer = TopMentionsSerializer(top_mentioned, many=True)
    return Response(serializer.data)