from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def ProductView(request, format=None):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method =='POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def Product_manage(request, id, format=None):
    
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






























# from product.models import Product
# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.core.serializers import serialize
# import json

# def show_product(request, format=None):
#     if(request.method == "GET"):
#         showall=json.loads(serialize("json",Product.objects.all()))
#         return JsonResponse(showall,safe=False, status=200)

# def post(request):
#         request_data = json.loads(request.body.decode('utf-8'))
#         saverecord=Product()
#         saverecord.name=request_data.get('name')
#         saverecord.color=request_data.get('color')
#         saverecord.price=request_data.get('price')
#         saverecord.save()
#         return JsonResponse(request,safe=False, status=201)

# def get(request, id):
#     try:
#         showall=json.loads(serialize("json",Product.objects.filter(id=id)))
#         return JsonResponse(showall, status=200)
#     except:
#         return JsonResponse({"error": "The id you are giveng to does not exist"}, status=404)

# def put(request, id):
#     try:
#         request_data = json.loads(request.body.decode('utf-8'))
#         saverecord = Product.objects.get(id=id)
#         saverecord.name=request_data.get('name')
#         saverecord.color=request_data.get('color')
#         saverecord.price=request_data.get('price')
#         saverecord.save()
#         return JsonResponse(request, status=200)
#     except:
#         return JsonResponse({"error": "the id you are giveng to change does not exist"}, status=404, safe=False)  

# def delete(request, id):
#     try:
#         saverecord = Product.objects.get(id=id)
#         saverecord.delete()
#         return JsonResponse({"deleted": True}, status=204, safe=False)
#     except:
#         return JsonResponse({"error": "given id does not exist"}, status=404, safe=False)
