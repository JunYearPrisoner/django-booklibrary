from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=64, null=False)
    Email = models.CharField(max_length=64, null=False)
    PassWord = models.CharField(max_length=64, null=False)
    IsManager = models.IntegerField(max_length=11)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=64, null=False)
    Author = models.CharField(max_length=64, null=False)
    Price = models.CharField(max_length=64, null=False)
    Publisher = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    IsReadOnline = models.CharField(max_length=64, null=False)
    BookNum = models.IntegerField(max_length=11)


class Cord(models.Model):
    id = models.AutoField(primary_key=True)
    UserName = models.IntegerField(max_length=11)
    BookName = models.IntegerField(max_length=11)
    ReturnTime = models.DateTimeField()
    State = models.IntegerField(max_length=11)

    