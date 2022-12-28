from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product
import json

class Testviews(TestCase):

    def setUp(self):
        self.client=Client()
        self.show_url = reverse('product')
        self.post_url = reverse('add_product')
        

    def test_show_product_GET(self):
        response = self.client.get(self.show_url)
        self.assertEquals(response.status_code, 200)

    

