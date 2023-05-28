from django.db import models
from django.conf import settings
# Create your models here.


class Article(models.Model):
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=100)
  content = models.TextField()
  published_date = models.DateTimeField()
  url = models.URLField(max_length=200)
  
  def __str__(self):
    return self.title

class UserNewsArticle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    news_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # You can add more fields here that relate to the user's interaction with the article
