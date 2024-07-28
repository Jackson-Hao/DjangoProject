from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from jsonpath import jsonpath
from rest_framework.views import APIView
import json
from .models import UserInfo, Book, LendBook

def login(request):
    # 获取请求参数
    data = json.loads(request.body)
    account = data.get("account")
    password = data.get("password")
    user = UserInfo.objects.filter(account=account, password=password).exists()
    if user:
        return JsonResponse({"message":"Success"})
    else:
        return JsonResponse({"message":"Failed"})

def regster(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        account = data.get("account")
        password = data.get("password")
        name = data.get("name")
        age = data.get("age")
        gender = data.get("gender")
        career = data.get("career")
        date = data.get("date")
        if (UserInfo.objects.filter(account=account).exists()):
            return JsonResponse({'message':'User existed'})            
        else:
            UserInfo.objects.create(account=account, password=password, name=name, age=age, gender=gender, career=career, date=date)
            return JsonResponse({'message': 'Success'})

def lend_book(request):
    data = json.loads(request.body)
    user = data.get("user_account")
    userstatus=UserInfo.objects.filter(account=user).exists()
    if(userstatus):
        book_num = data.get("book_num")
        LendBook.objects.create(user_account=user, book_num=book_num, lend_date=timezone.now())
        return JsonResponse({'message':'Success!'})
    else:
        return JsonResponse({'message':'Failed!'})

def return_book(request):
    data = json.loads(request.body)
    user = get_object_or_404(UserInfo, account=data.get("user_account"))
    book = get_object_or_404(LendBook, user_account=data.get("user_account"), book_num=data.get("book_num"))
    book.delete()
    return JsonResponse({'message':'Success!'})

# -------------------------------------------------------------------------------------------------------------
def book_creat(request):
    data = json.loads(request.body)
    Book.objects.create(num=data.get("num"), name=data.get("name"), author=data.get("author"), date=data.get("date"))
    return JsonResponse({'message':'Success!'})

def book_delete(request):
    data=json.loads(request.body)
    num=data.get('num')
    book = get_object_or_404(Book, num=num)
    book.delete()
    return JsonResponse({'message':'Success!'})

def book_update(request):
    data=json.loads(request.body)
    num=data.get('num')
    name=data.get('name')
    author=data.get('author')
    date=data.get('date')
    book = get_object_or_404(Book, num=num)
    book.name = name
    book.author = author
    book.date = date
    book.save()
    return JsonResponse({'message':'Success'})

def book_query(request):
    data=json.loads(request.body)
    num=data.get('num')
    book = Book.objects.filter(num=num)
    return JsonResponse({'Book: ':book})