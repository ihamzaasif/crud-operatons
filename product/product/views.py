from .models import Product,GetQuerySet
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
import django_filters
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.core.cache import cache

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    color = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='exact')
    class Meta:
        model = Product
        fields = ['name','color','price']

class ProductView(ListAPIView, CreateAPIView):
    
    queryset = Product.objects.filter_by_color_and_price()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)     

class ProductManage(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView, APIView):
    queryset = Product.objects.select_related('user').filter(user__username='username')
    queryset = Product.objects.prefetch_related('user')
    serializer_class = ProductSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)       

    def delete(self, request, pk):
        return self.destroy(request, pk)
