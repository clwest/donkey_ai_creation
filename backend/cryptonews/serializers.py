# serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

class CryptoNewsSerializer(serializers.Serializer):
    news_url = serializers.URLField()
    image_url = serializers.URLField()
    title = serializers.CharField()
    text = serializers.CharField()
    source_name = serializers.CharField()
    date = serializers.DateField()
    topics = serializers.ListField(child=serializers.CharField())
    sentiment = serializers.CharField()
    type = serializers.CharField()


class CryptoNewsSourceSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.CharField()


class TrendingSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  headline = serializers.CharField()
  text = serializers.CharField()
  news_id = serializers.IntegerField()
  date = serializers.DateField()
  sentiment = serializers.CharField(allow_null=True)
  tickers = serializers.ListField(child=serializers.CharField(allow_null=True))



class EventSerializer(serializers.Serializer):
    event_name = serializers.CharField()
    event_text = serializers.CharField()
    event_id = serializers.CharField()
    news_items = serializers.IntegerField()
    date = serializers.CharField()
    tickers = serializers.ListField(child=serializers.CharField())
    articles = serializers.ListField(child=serializers.DictField())

  
class TopMentionsSerializer(serializers.Serializer):
  total_mentions = serializers.IntegerField()
  positive_mentions = serializers.IntegerField()
  negative_mentions = serializers.IntegerField()
  ticker = serializers.CharField()
  name = serializers.CharField()
  sentiment_score = serializers.FloatField()

class AllTickersNewsSerializer(serializers.Serializer):
  news_url = serializers.URLField()
  image_url = serializers.URLField()
  title = serializers.CharField()
  text = serializers.CharField()
  source_name = serializers.CharField()
  date = serializers.CharField()
  topics = serializers.ListField(child=serializers.CharField(allow_null=True))
  sentiment = serializers.CharField()
  type = serializers.CharField()
  tickers = serializers.ListField(child=serializers.CharField(allow_null=True))