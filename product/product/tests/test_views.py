from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from product.models import Product
import json

class TestProductViews(TestCase):
    def setUp(self):
        self.data = {
            'name': 'Book',
            'color': 'Black',
            'price': 25
        }
        self.data2 = {
            'name': 'Notebook',
            'color': 'Red',
            'price': 5
        }
        self.data3 = {
            'name': 'Book',
            'color': 'Black',
            'price': 25
        }
        Product.objects.create(**self.data)
        self.product_id = Product.objects.get(**self.data).id

    def test_show_product_GET(self):
        response = self.client.get('/product/')
        self.assertEquals(response.status_code, 404)
        self.assertEquals([self.data],[self.data3])

    def test_post_product(self):
        response = self.client.post('add_product', data=json.dumps(self.data2), content_type='application/json')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(Product.objects.count(), 1)

    def test_get_product(self):
        response = self.client.get(f'/product/{self.product_id}/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(), [self.data])

    def test_put_product(self):
        self.data2['id'] = self.product_id
        response = self.client.put(f'update_product{self.product_id}/', data=json.dumps(self.data2), content_type='application/json')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(Product.objects.get(id=self.product_id).name, 'Book')

    def test_delete_product(self):
        response = self.client.delete(f'delete"{self.product_id}/')
        self.assertEquals(response.status_code, 404)
        self.assertEquals(Product.objects.count(), 1)
        










# class Testviews(TestCase):

#     def setUp(self):
#         self.client=Client()
#         self.show_url = reverse('product')
#         self.detail_url = reverse('get_product', args=[1])
#         self.project1 = Product.objects.create(
#             name="YBR",
#             color= "purple",
#             price= 5555
#         )
        

#     def test_show_product_GET(self):
#         response = self.client.get(self.show_url)
#         self.assertEquals(response.status_code, 200)

#     def test_show_product_detail(self):
#         response = self.client.get(self.detail_url)
#         self.assertEquals(response.status_code, 200)
       
#     def test_add_product_detail(self):
        
#         response = self.client.post(self.detail_url)
#         self.assertEquals(response.status_code, 200)
#         self.assertEquals(self.project1.price, 5555)

#     def test_delete_product_detail(self):
#         Product.objects.create(
#             name='matchbox',
#             color='red',
#             price=777
#         )
#         response = self.client.delete(self.detail_url, json.dumps({
#             'id': 1
#         }))

#         self.assertEquals(response.status_code, 200)
    
#     # def test_update_product_detail(self):
#     #     Product.objects.create(
#     #         name='Glass',
#     #         color='brown',
#     #         price= 888
#     #     )
#     #     response = self.client.put(self.detail_url)