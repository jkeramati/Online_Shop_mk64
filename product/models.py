from django.db import models
from core.models import *
from discount.models import Discount
from comment.models import Comment


# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    category = models.ManyToManyField('Category')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    description = models.TextField()
    discount = models.ForeignKey(to=Discount, on_delete=models.CASCADE)
    image = models.FileField()
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE)


class Category(BaseModel):
    name = models.CharField(max_length=50)
    category = models.OneToOneField('self', on_delete=models.CASCADE)


class Brand(BaseModel):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20, null=True, blank=True)
