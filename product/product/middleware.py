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
        
        if hasattr(response, 'data'):
            content = response.data
        else:
            content = response.content
        
        if product:
            print("Middle ware cache is called")
            return response

        if response.status_code == 200:
            cache.set(cache_key, content, timeout=3600)
        
        return response