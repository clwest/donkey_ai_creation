from django.test import TestCase

# Create your tests here.
from django.test import Client
client = Client()
response = client.get('/api/v1/coins')
print(response.status_code)