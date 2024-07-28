from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from jsonpath import jsonpath
from rest_framework.views import APIView
from .models import User
from .models import animal
from .models import Led
from .models import book
from .models import user_borrowed
import json

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.auth.credentials import DerivedCredentials
from huaweicloudsdkcore.region.region import Region as coreRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *




def login_verify(request):
    # 获取请求参数
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    user = user_borrowed.objects.filter(username=username, password=password).exists()
    if user:
        print("\033[32m{} {} {} \033[0m".format("User:",username,"login successful"))
        return JsonResponse({"message": "successful"})
    else:
        print("\033[31m{} {} {} \033[0m".format("User:",username,"login failed"))
        return JsonResponse({"message": "failed"})

def user_search(request):
    data = json.loads(request.body)
    username = data.get("username")
    user = user_borrowed.objects.filter(username=username).exists()
    if user:
        return JsonResponse({"message": "successful"})
    else:
        return JsonResponse({"message": "failed"})

def regster(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        if user_borrowed.objects.filter(username=username).exists():
            return JsonResponse({'message': 'existed'})
        else:
            user_borrowed.objects.create(username=username, password=password, userright='A', borrow_bid='0')
            return JsonResponse({'message': 'successful'})


# def get_animals(request):
#     animals = animal.objects.all()
#     animals_list = [{'name': animal.name, 'num': animal.num} for animal in animals]
#     return JsonResponse({'animal': animals_list})

def led_status(request):
    status_db = Led.objects.values('status')
    buff = list(status_db.values())
    buff1 = list(buff[0].values())
    return JsonResponse({'status': '{}'.format(buff1[1])})


def book_verify(request):
    data = json.loads(request.body)
    bookname = data.get("bookname")
    author = data.get("author")
    status = book.objects.filter(bookname=bookname, author=author).exists()
    if status:
        return JsonResponse({"message": "exist"})
    else:
        return JsonResponse({"message": "not exist"})


def book_creat(request):
    data = json.loads(request.body)
    bookname = data.get("bookname")
    author = data.get("author")
    if book.objects.filter(bookname=bookname).exists():
        return JsonResponse({'message': 'existed'})
    else:
        book.objects.create(bookname=bookname, author=author)
        return JsonResponse({'message': 'successful'})

def checkNetwork(request):
    print("\033[32m{} \033[0m".format("APP Network connect successful"))
    return HttpResponse(200)

def led_control(request):
    data = json.loads(request.body)
    status = data.get("message")
    print("Message recieve!")
    ak = "K3AHSXRVMNIIUTINGDFI"
    sk = "3oR05oeKteQXUQAXTvThtQzODd5xkfdpBLJrikgQ"
    iotdaEndpoint = "51a2c7fd9b.st1.iotda-app.cn-north-4.myhuaweicloud.com";

    credentials = BasicCredentials(ak, sk).with_derived_predicate(DerivedCredentials.get_default_derived_predicate())

    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(coreRegion(id="cn-north-4", endpoint=iotdaEndpoint)) \
        .build()

    try:
        request = CreateCommandRequest()
        request.device_id = "6613b0b82ccc1a58388044e4_Hi3861V100"
        if(status == "ON"):
            request.body = DeviceCommandRequest(
                paras="{\"status\":\"ON\"}",
                command_name="LED_Control",
                service_id="ADC"
            )
        elif(status == "OFF"):
            request.body = DeviceCommandRequest(
                paras="{\"status\":\"OFF\"}",
                command_name="LED_Control",
                service_id="ADC"
            )
        elif(status == "SPARK"):
            request.body = DeviceCommandRequest(
                paras="{\"status\":\"SPARK\"}",
                command_name="LED_Control",
                service_id="ADC"
            )
        print("\033[34m {} \033[0m".format(request))
        response = client.create_command(request)
        print("\033[32m {} \033[0m".format(response))
        return JsonResponse({"message":"successful"})
    except exceptions.ClientRequestException as e:
        print("{}   {}  {}".format(e.status_code,e.request_id,e.error_code))
        print("\033[31mERR:{}\033[0m".format(e.error_msg))
        return JsonResponse({"message":"failed"})

def alarm(request):
    data = json.loads(request.body)
    status = data.get("message")
    print("Message recieve!")
    ak = "K3AHSXRVMNIIUTINGDFI"
    sk = "3oR05oeKteQXUQAXTvThtQzODd5xkfdpBLJrikgQ"
    iotdaEndpoint = "51a2c7fd9b.st1.iotda-app.cn-north-4.myhuaweicloud.com";

    credentials = BasicCredentials(ak, sk).with_derived_predicate(DerivedCredentials.get_default_derived_predicate())

    client = IoTDAClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(coreRegion(id="cn-north-4", endpoint=iotdaEndpoint)) \
        .build()

    try:
        request = CreateCommandRequest()
        request.device_id = "6613b0b82ccc1a58388044e4_Hi3861V100"
        if(status == "ON"):
            request.body = DeviceCommandRequest(
                paras="{\"status\":\"ON\"}",
                command_name="Alarm",
                service_id="ADC"
            )
        elif(status == "OFF"):
            request.body = DeviceCommandRequest(
                paras="{\"status\":\"OFF\"}",
                command_name="Alarm",
                service_id="ADC"
            )
        print("\033[34m {} \033[0m".format(request))
        response = client.create_command(request)
        print("\033[32m {} \033[0m".format(response))
        return JsonResponse({"message":"successful"})
    except exceptions.ClientRequestException as e:
        print("{}   {}  {}".format(e.status_code,e.request_id,e.error_code))
        print("\033[31mERR:{}\033[0m".format(e.error_msg))
        return JsonResponse({"message":"failed"})

