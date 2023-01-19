from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Product(models.Model):
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()
    class Meta:
        db_table="pro"

# valu = input('Enter the color: ')
# def Color_find():
#     Color_products = Product.objects.filter(color__iexact=valu)
#     if len(Color_products) == 0:
#         print("No product found with this color")
#     else:
#         for product in Color_products:
#             print("ID of the product is " + str(product.pk))
#             print("Product name is " + product.name)
# Color_find()


# def Price_Search():
#     val_for_price = int(input('Enter the Price: '))
#     price_products = Product.objects.filter(price__gt=val_for_price)
#     if len(price_products) == 0:
#         print("No product found with the entered price: " + str(val_for_price))
#     else:
#         for product in price_products:
#             print("ID of the product which is greeater then price "+str(val_for_price)+" is "+ str(product.pk))
#             print("Product name is " + product.name + "\n Product price " + str(product.price))
# Price_Search()