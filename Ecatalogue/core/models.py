from django.db import models

import uuid 

"""class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, db_index=True)
    username = models.CharField(max_length=50, blank=False, db_index=True)
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    phonenumber = models.CharField(max_length=12)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    Profil = models.ImageField(upload_to="img/User_images/", default=None, null=True) 
    
    def __str__(self):
        return self.username"""
    
    
"""class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, db_index=True)
    name = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.name"""


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, db_index=True)
    name = models.CharField(max_length=200, null= False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=600)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="img/Product_images/", default=None, null=True)
    category = models.CharField(max_length=200, null=False)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, db_index=True)
    name = models.CharField(max_length=200, null=False)
    