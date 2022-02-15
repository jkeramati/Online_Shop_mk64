from django.db import models

import product.models
from core.models import *
from discount.models import Discount
from comment.models import Comment


# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ManyToManyField('Category', null=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    discount = models.ForeignKey(to=Discount, on_delete=models.CASCADE, null=True, blank=True)
    image = models.FileField(null=True, default=None, upload_to='product/')
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE, null=True, blank=True)


class Category(BaseModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


class Brand(BaseModel):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20, null=True, blank=True)
