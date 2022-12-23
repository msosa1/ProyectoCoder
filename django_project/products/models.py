from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField()
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)