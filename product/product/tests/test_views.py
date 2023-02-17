from django.utils import timezone
import jwt
from rest_framework.test import APITestCase
from product.models import Product
from django_filters import FilterSet, CharFilter
import json
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
from datetime import timedelta
from django.contrib.auth.models import User

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, timedelta):
            return str(obj)
        return super().default(obj)

class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name']

class TestProductViews(APITestCase):
    fixtures = ['product_data.json']

    def setUp(self):
        self.product_id = Product.objects.get(pk=1).pk
        self.user = User.objects.create_user(username='hamzaa', password='hamzaasif')
        access_token = str(AccessToken.for_user(self.user))
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        self.product_id = Product.objects.create(user=self.user, name='TV', color='black', price=1234).id

    def test_show_product_GET(self):
        response = self.client.get('/', format='json')
        data = response.json()
        self.assertEquals(response.status_code, 200)
        expected_data = [{'id': 8, 'user': 'hamzaa', 'name': 'TV', 'color': 'black', 'price': 1234}]
        self.assertEquals(data, expected_data)

        #Test scenario for getting product by name
        response = self.client.get('/', {'name': 'lcd'})
        data = response.json()
        self.assertEquals(response.status_code, 200)
        expected_data = [{'id': 8, 'user': 'hamzaa', 'name': 'TV', 'color': 'black', 'price': 1234}]
        self.assertEquals(data, expected_data)

        #Test scenario for getting product by their color
        response = self.client.get('/', {'color': 'green'})
        data = response.json()
        self.assertEquals(response.status_code, 200)
        expected_data = [{'id': 8, 'user': 'hamzaa', 'name': 'TV', 'color': 'black', 'price': 1234}]
        self.assertEquals(data, expected_data)

        #Test scenario for getting product by both name and color
        response = self.client.get('/', {'name': 'mug', 'color': 'green'})
        data = response.json()
        self.assertEquals(response.status_code, 200)
        expected_data = [{'id': 8, 'user': 'hamzaa', 'name': 'TV', 'color': 'black', 'price': 1234}]
        self.assertEquals(data, expected_data)

        #Test scenario for getting product by price
        response = self.client.get('/', {'price': 5555})
        data = response.json()
        self.assertEquals(response.status_code, 200)
        expected_data = [{'id': 8, 'user': 'hamzaa', 'name': 'TV', 'color': 'black', 'price': 1234}]
        self.assertEquals(data, expected_data)

    def test_post_product(self):
        data = {'name': 'LCD', 'description': 'HD', 'price': 4444, 'user_id': self.user.id}
        response = self.client.post('/', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 400)
        self.assertEquals(Product.objects.count(), 3)
    
    def test_get_product(self):
        response = self.client.get(f'/{self.product_id}')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, {'id': 4, 'user': 'hamzaa', 'name': 'TV', 'color': 'black', 'price': 1234})
        
        #Test scenario for invalid id
        response = self.client.get(f'/6')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})

        #Test scenario for string type
        response = self.client.get(f'/ab')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})

    def test_put_product(self):
        data = {'name': 'LCD', 'color': 'HD', 'price': 4444}
        response = self.client.put(f'/{self.product_id}', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Product.objects.get(id=self.product_id).name,'LCD')

        #Test scenario for invalid id
        response = self.client.put(f'/8', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})

        #Test scenario for String type
        response = self.client.put(f'/ab', data=json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})

    def test_delete_product(self):
        response = self.client.delete(f'/{self.product_id}')
        self.assertEquals(response.status_code, 204)
        self.assertIsNone(Product.objects.filter(id=self.product_id).first())

        #Test scenario for invalid id
        response = self.client.delete(f'/8')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})

        #Test scenario for invalid id
        response = self.client.delete(f'/ab')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(response.data, {"detail": "Not found."})