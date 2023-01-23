from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class SearchColor(models.Manager):
    def get_queryset(self, valu=None):
        return super().get_queryset().filter(color__iexact=valu)

class SearchPrice(models.Manager):
    def get_queryset(self, valu_for_price=None):
        return super().get_queryset().filter(price__gt=valu_for_price)
        
        
class Product(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()
    class Meta:
        db_table="pro"
    objects = models.Manager()
    object_color = SearchColor()
    object_price = SearchPrice()

valu = input('Enter the color: ')
products = Product.object_color.get_queryset(valu)

if not products:
    print("No product found with this color")
else:
    for product in products:
        print("ID of the product is " + str(product.pk))
        print("Product name is " + product.name)
        print("Product price is"+ str(product.price))


valu_for_price = input('\n Enter the price: ')
products1 = Product.object_price.get_queryset(valu_for_price)
if not products1:
    print("No product found with the given price")
else:
    for product in products1:
        print("ID of the product is " + str(product.pk))
        print("Product name is " + product.name)
        print("product color is " + product.color)
        print("product color is " + str(product.price))
