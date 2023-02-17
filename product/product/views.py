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
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    color = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='exact')
    class Meta:
        model = Product
        fields = ['name','color','price']

class ProductView(ListAPIView, CreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise AuthenticationFailed()
        user_id = self.request.user.id
        return Product.objects.filter(user_id=user_id).select_related('user').prefetch_related('user')
        
    def get(self, request, pk=None):
        cache_key = "product_list"
        result = cache.get(cache_key)
        if result:
            return Response(result)
        result = self.list(request)
        cache.set(cache_key, result.data, timeout=3600)
        return result


    def post(self, request):
        return self.create(request)     

class ProductManage(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView, APIView):
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise AuthenticationFailed()
        user_id = self.request.user.id
        return Product.objects.filter(user_id=user_id).select_related('user').prefetch_related('user')

    def get(self, request, pk):
        cache_key = f"product_{pk}"
        result = cache.get(cache_key)
        print("redis")
        if result:
            return Response(result)
        result = self.retrieve(request, pk)
        cache.set(cache_key, result.data, timeout=3600)
        print("database")
        return result

    def put(self, request, pk):
        return self.update(request, pk)       

    def delete(self, request, pk):
        return self.destroy(request, pk)
