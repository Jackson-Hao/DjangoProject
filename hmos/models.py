from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class animal(models.Model):
    name = models.CharField(max_length=100)
    num = models.CharField(max_length=100)


class Led(models.Model):
    status = models.CharField(max_length=1)


class book(models.Model):
    bid = models.CharField(max_length=8)    # 书本id，手动指定，但不得重复且不得为0
    bookname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

class user_borrowed(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    userright = models.CharField(max_length=1,default="A")  # A:Admin R:Root
    borrow_bid = models.CharField(max_length=8,default="0")   # 借书的id
