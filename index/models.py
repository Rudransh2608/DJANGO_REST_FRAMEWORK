from django.db import models
from django.contrib.auth.models import User 

class Freak(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    Phone=models.PositiveIntegerField()

class Category(models.Model):
    category_name = models.CharField(max_length=100)

class book(models.Model):
    books=models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title=models.CharField(max_length=100)

def __str__(self):
        return self.book