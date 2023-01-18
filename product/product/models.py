from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Product(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()
    class Meta:
        db_table="pro"


try:
    val = input('Enter the color: ')
    Color_products = Product.objects.filter(color__iexact=val)
    for product in Color_products:
        print("ID of the product is " + str(product.pk))
        print("Product name is " + product.name)

except ObjectDoesNotExist as e:
    print("No product found with this color: ", e)

try:
    val = int(input('Enter the Price: '))
    price_products = Product.objects.filter(price__gt=val)
    if len(price_products) == 0:
        raise ValueError("No product found with the entered price: " + val)
    else:
        for product in price_products:
            print("ID of the product which is greeater then price "+val+" is "+ str(product.pk))
            print("Product name is " + product.name + "\n Product price " + str(product.price))
except ValueError as e:
    print(e)