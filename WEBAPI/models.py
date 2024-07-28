from django.db import models

class UserInfo(models.Model):
    account = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=4)
    career = models.CharField(max_length=18)
    date = models.CharField(max_length=24)

class Book(models.Model):
    num=models.CharField(max_length=6,unique=True)
    name=models.CharField(max_length=12)
    author=models.CharField(max_length=16)
    date=models.CharField(max_length=24)
    
from WEBAPI.models import UserInfo
class LendBook(models.Model):
    user_account = models.ForeignKey(UserInfo, on_delete=models.CASCADE, to_field='account', db_column='user_account')
    book_num = models.ForeignKey(Book, on_delete=models.CASCADE, to_field='num',db_column='book_num')
    lend_date=models.CharField(max_length=24)
# Create your models here.
