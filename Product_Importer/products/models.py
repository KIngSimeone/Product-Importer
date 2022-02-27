from re import T
from django.db import models

class Products(models.Model):
    name = models.TextField(null=True)
    sku = models.TextField(null=True, unique=True)
    description = models.TextField(null=True)
    
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)