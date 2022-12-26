from product.models import PrModel
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json

@csrf_exempt
def showpr(request, format=None):
    if(request.method == "GET"):
        showall=json.loads(serialize("json",PrModel.objects.all()))
        return JsonResponse({'products': showall})

    elif(request.method == "POST"):
        request_data = json.loads(request.body.decode('utf-8'))
        request_data.get('prname') and request_data.get('prcolor') and request_data.get('price')
        saverecord=PrModel()
        saverecord.prname=request_data.get('prname')
        saverecord.prcolor=request_data.get('prcolor')
        saverecord.price=request_data.get('price')
        saverecord.save()
        return HttpResponse(request)

@csrf_exempt
def get(request, id):
    showall=json.loads(serialize("json",PrModel.objects.filter(id=id)))
    return JsonResponse(showall,safe=False)

@csrf_exempt
def put(request, id):
    print ("hello")
    request_data = json.loads(request.body.decode('utf-8'))
    request_data.get('prname') and request_data.get('prcolor') and request_data.get('price')
    saverecord = PrModel.objects.get(id=id)
    saverecord.prname=request_data.get('prname')
    saverecord.prcolor=request_data.get('prcolor')
    saverecord.price=request_data.get('price')
    saverecord.save()
    return HttpResponse(request,)    

@csrf_exempt
def delete(request, id):
    try:
        saverecord = PrModel.objects.get(id=id)
        saverecord.delete()
        return JsonResponse({"deleted": True}, safe=False)
    except:
        return JsonResponse({"error": "not a valid primary key"}, safe=False)


    
        


    
   



    
  
    
