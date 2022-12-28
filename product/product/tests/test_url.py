from django.test import SimpleTestCase
from django.urls import reverse,resolve
from product.views import show_product,post,get,put,delete

class TestUrls(SimpleTestCase):

    def test_product_url_is_resolved(self):
        url = reverse('product')
        print(resolve(url))
        self.assertEqual(resolve(url).func,show_product)
    
    def test_product_url_is_resolved(self):
        url = reverse('add_product')
        print(resolve(url))
        self.assertEqual(resolve(url).func,post)
    
    def test_product_url_is_resolved(self):
        url = reverse('get_product',args=[50])
        print(resolve(url))
        self.assertEqual(resolve(url).func,get)

    def test_product_url_is_resolved(self):
        url = reverse('update_product',args=[50])
        print(resolve(url))
        self.assertEqual(resolve(url).func,put)

    def test_product_url_is_resolved(self):
        url = reverse('delete',args=[50])
        print(resolve(url))
        self.assertEqual(resolve(url).func,delete)