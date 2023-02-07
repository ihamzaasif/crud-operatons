from django.core.cache import cache
from rest_framework.response import Response

class CacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cache_key = f"product_{pk}"
        product = cache.get(cache_key)
        response = self.get_response(request, *args, **kwargs)
        if product:
            print("middle ware cache called")
            return response