from django.db import models
from django.conf import settings
# Create your models here.


class Article(models.Model):
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=100)
  content = models.TextField()
  published_date = models.DateTimeField()
  url = models.URLField(max_length=200)
  user = models.ManyToManyField(settings.AUTH_USER_MODEL)
  
  def __str__(self):
    return self.title