from django.db import models

class PrModel(models.Model):
    prname=models.CharField(max_length=100)
    prcolor=models.CharField(max_length=100)
    price=models.IntegerField()
    class Meta:
        db_table="pro"