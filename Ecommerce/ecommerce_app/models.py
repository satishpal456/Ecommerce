from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    stock_status = [
        ("IN STOCK", "IN STOCK"),
        ("OUT OF STOCK", "OUT OF STOCK")
    ]

    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField(null=True,default=0)
    actual_mrp = models.IntegerField(null=True, default=0)
    quatity = models.IntegerField(null=True, default=0)
    stock = models.CharField(choices=stock_status, max_length=255, null=True, blank=False)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)
    is_deleted = models.BooleanField(default=True)

class CartProducts(models.Model):
    user = models.ForeignKey(to=User, null=True,  on_delete=models.CASCADE, related_name='user')
    product = models.ForeignKey(to=Product, null=True,  on_delete=models.CASCADE, related_name='product')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)
    is_deleted = models.BooleanField(default=True)