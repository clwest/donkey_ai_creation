
from django.db import models

class Coin(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    # ... any other fields you need to store
