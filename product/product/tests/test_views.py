from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product
from django.core.management import call_command
import json

class TestProductViews(TestCase):
    fixtures = ['product_data.json']

    def setUp(self):
        call_command('loaddata', 'product_data.json')
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
        Product.objects.create(self.data)
        self.product_id = Product.objects.get(self.data).id

    def test_show_product_GET(self):
        response = self.client.get('/product/?name=teest')
        data =response.json()
        self.assertEquals(response.status_code, 404)
        self.assertEqual(data[0]['name'], 'testproduct')

    def test_post_product(self):
        # create product
        response = self.client.post('add_product', data=json.dumps(self.data2), content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(Product.objects.count(), 1)
        # create product with duplicate data
        self.assertEqual()

    def test_get_product(self):
        response = self.client.get(f'/product/{self.product_id}/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual([self.data3], [self.data])

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