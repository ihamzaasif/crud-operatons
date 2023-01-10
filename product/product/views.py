from product.models import Product
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json

def show_product(request, format=None):
    if(request.method == "GET"):
        showall=json.loads(serialize("json",Product.objects.all()))
        return JsonResponse(showall,safe=False, status=200)

def post(request):
        request_data = json.loads(request.body.decode('utf-8'))
        saverecord=Product()
        saverecord.name=request_data.get('name')
        saverecord.color=request_data.get('color')
        saverecord.price=request_data.get('price')
        saverecord.save()
        return JsonResponse(request,safe=False, status=201)

def get(request, id):
    try:
        showall=json.loads(serialize("json",Product.objects.filter(id=id)))
        return JsonResponse(showall, status=200)
    except:
        return JsonResponse({"error": "The id you are giveng to does not exist"}, status=404)

def put(request, id):
    try:
        request_data = json.loads(request.body.decode('utf-8'))
        saverecord = Product.objects.get(id=id)
        saverecord.name=request_data.get('name')
        saverecord.color=request_data.get('color')
        saverecord.price=request_data.get('price')
        saverecord.save()
        return JsonResponse(request, status=200)
    except:
        return JsonResponse({"error": "the id you are giveng to change does not exist"}, status=404, safe=False)  

def delete(request, id):
    try:
        saverecord = Product.objects.get(id=id)
        saverecord.delete()
        return JsonResponse({"deleted": True}, status=204, safe=False)
    except:
        return JsonResponse({"error": "given id does not exist"}, status=404, safe=False)
