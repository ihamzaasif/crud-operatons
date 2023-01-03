from django.test import TestCase
from product.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="Product 1", color="Red", price=10)
        Product.objects.create(name="Product 2", color="Blue", price=20)

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