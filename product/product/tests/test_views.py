from rest_framework.test import APITestCase
from django.urls import reverse
from product.models import Product
import django_filters
from django_filters import FilterSet, CharFilter
from django.core.management import call_command
import json

class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name']
    
class TestProductViews(APITestCase):
    fixtures = ['product_data.json']

    def setUp(self):
        self.product_id = Product.objects.get(pk=1).pk

    def test_name_filter(self):
        queryset = Product.objects.all()
        filtered_queryset = ProductFilter({'name': 'lcd'}, queryset=queryset).qs
        data1 = filtered_queryset.values()
        self.assertEquals(data1[0], {'id': 1, 'name': 'LCD', 'color': 'HD', 'price': 4444})
        
    def test_color_filter(self):
        queryset = Product.objects.all()
        filtered_queryset = ProductFilter({'color': 'hd'}, queryset=queryset).qs
        data1 = filtered_queryset.values()
        self.assertEquals(data1[0], {'id': 1, 'name': 'LCD', 'color': 'HD', 'price': 4444})

    def test_combined_filter(self):
        queryset = Product.objects.all()
        filtered_queryset = ProductFilter({'name': 'LCD', 'color': 'HD'}, queryset=queryset).qs
        data1 = filtered_queryset.values()
        self.assertEquals(data1[0], {'id': 1, 'name': 'LCD', 'color': 'HD', 'price': 4444})

    def test_show_product_GET(self):
        response = self.client.get('/')
        data = response.json()
        self.assertEquals(response.status_code, 200)
        expected_data = [{'id': 1, 'name': 'LCD', 'color': 'HD', 'price': 4444},{'id': 2, 'name': 'mug', 'color': 'green', 'price': 5555}]
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





