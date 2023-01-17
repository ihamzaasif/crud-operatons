from rest_framework.test import APITestCase
from django.urls import reverse
from product.models import Product
from django.core.management import call_command
import json

class TestProductViews(APITestCase):
    fixtures = ['product_data.json']

    def setUp(self):
        Product.objects.create(name="LCD",color="HD", price=4444)
        self.product_id = Product.objects.get(pk=1).pk

    def test_show_product_GET(self):
        response = self.client.get('/')
        data = response.json()
        self.assertEquals(response.status_code, 200)
        expected_data = [{'id': 1, 'name': 'LCD', 'color': 'HD', 'price': 4444}, {'id': 7, 'name': 'LCD', 'color': 'HD', 'price': 4444}]
        self.assertEquals(data, expected_data)

    def test_post_product(self):
        data = {'name': 'LCD', 'color': 'HD', 'price': 4444}
        response = self.client.post('/', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(Product.objects.count(), 3)

    def test_get_product(self):
        response = self.client.get(f'/{self.product_id}')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, {'id': 1, 'name': 'LCD', 'color': 'HD', 'price': 4444})
        
        #Test scenario for invalid id
        response = self.client.get(f'/6')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {'error': 'Product not found'})

        #Test scenario for string type
        response = self.client.get(f'/ab')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {'error': 'Invalid string type'})

    def test_put_product(self):
        data = {'name': 'LCD', 'color': 'HD', 'price': 4444}
        response = self.client.put(f'/{self.product_id}', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Product.objects.get(id=self.product_id).name,'LCD')

        #Test scenario for invalid id
        response = self.client.put(f'/8', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {'error': 'Product not found'})

        #Test scenario for String type
        response = self.client.put(f'/abc', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {'error': 'Invalid string type'})

    def test_delete_product(self):
        response = self.client.delete(f'/{self.product_id}')
        self.assertEquals(response.status_code, 204)
        self.assertIsNone(Product.objects.filter(id=self.product_id).first())

        #Test scenario for invalid id
        response = self.client.delete(f'/8')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {'error': 'Product not found'})

        #Test scenario for invalid id
        response = self.client.delete(f'/ab')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {'error': 'Invalid string type'})