from django.db import models
from django.contrib.auth.models import User

class GetQuerySet(models.QuerySet):
    def get_queryset(self):
        return super().get_queryset().filter(color__iexact="red")
    
    def get_queryset(self):
        return super().get_queryset().filter(price__gt=200)
        
class SearchColor(models.Manager):
    def get_queryset(self):
        return GetQuerySet(self.model, using=self._db)

    def gets(self, valu=None):
        return super().get_queryset().filter(color__iexact=valu)
    
    def get_queryset(self):
        return Product.objects.filter(price__gt=50,color="red").order_by('name').limit(5)

class SearchPrice(models.Manager):
    def get_queryset(self):
        return GetQuerySet(self.model, using=self._db)

    def get_queryset(self, valu_for_price=None):
        return super().get_queryset().filter(price__gt=valu_for_price)
        
def get_default_user():
    return User.objects.get(username='username').pk

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_default_user)
    name=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    price=models.IntegerField()
    class Meta:
        db_table="pro"

 

    objects = models.Manager()
    object_color = SearchColor()
    object_price = SearchPrice()

