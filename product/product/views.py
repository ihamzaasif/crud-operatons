from product.models import Product
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
import json

def show_product(request, format=None):
    if(request.method == "GET"):
        showall=json.loads(serialize("json",Product.objects.all()))
        return HttpResponse(showall)

def post(request):
        request_data = json.loads(request.body.decode('utf-8'))
        saverecord=Product()
        saverecord.name=request_data.get('name')
        saverecord.color=request_data.get('color')
        saverecord.price=request_data.get('price')
        saverecord.save()
        return HttpResponse(request)


def get(request, id):
    showall=json.loads(serialize("json",Product.objects.filter(id=id)))
    return HttpResponse(showall)


def put(request, id):
    print ("hello")
    request_data = json.loads(request.body.decode('utf-8'))
    saverecord = Product.objects.get(id=id)
    saverecord.name=request_data.get('name')
    saverecord.color=request_data.get('color')
    saverecord.price=request_data.get('price')
    saverecord.save()
    return HttpResponse(request)    


def delete(request, id):
    try:
        saverecord = Product.objects.get(id=id)
        saverecord.delete()
        return JsonResponse({"deleted": True}, safe=False)
    except:
        return JsonResponse({"error": "not a valid primary key"}, safe=False)


    
        


    
   



    
  
    
