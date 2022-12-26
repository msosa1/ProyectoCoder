from django.db import models

# Create your models here.

#class Products(models.Model):
 #   name = models.CharField(max_length=100)
  #  price = models.FloatField()
   # stock = models.BooleanField()
    
    
class Family(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    relationship = models.CharField(max_length=200)
    alive = models.BooleanField()