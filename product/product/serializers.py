from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'