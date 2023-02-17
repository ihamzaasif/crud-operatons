from django.test import TestCase
from product.models import Product
from django.contrib.auth.models import User


class ProductTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="username", password="password")
        Product.objects.create(name="Product 1", color="Red", price=10, user=user)
        Product.objects.create(name="Product 2", color="Blue", price=20, user=user)

    def test_products_have_correct_names(self):
        product_1 = Product.objects.get(name="Product 1")
        product_2 = Product.objects.get(name="Product 2")
        self.assertEqual(product_1.name, "Product 1")
        self.assertEqual(product_2.name, "Product 2")

    def test_products_have_correct_prices(self):
        product_1 = Product.objects.get(name="Product 1")
        product_2 = Product.objects.get(name="Product 2")
        self.assertEqual(product_1.price, 10)
        self.assertEqual(product_2.price, 20)
    
    def test_products_have_correct_color(self):
        product_1 = Product.objects.get(color="Red")
        product_2 = Product.objects.get(color="Blue")
        self.assertEqual(product_1.color, "Red")
        self.assertEqual(product_2.color, "Blue")
        
    # def test_search_color(self):
    #     products = Product.object_color.get_queryset("Red")
    #     self.assertEqual(len(products), 1)
    #     self.assertEqual(products[0].name, "Product 1")
        
    def test_search_price(self):
        products = Product.object_price.get_queryset(2)
        self.assertEqual(len(products), 2)
        self.assertEqual(products[0].price, 10)
        self.assertEqual(products[1].price, 20)