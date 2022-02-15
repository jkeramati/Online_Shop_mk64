from django.db import models
from core.models import *
from costumer.models import Costumer
from discount.models import Discount

# Create your models here.
from product.models import Product


class Cart(BaseModel):
    costumer = models.ForeignKey(to=Costumer, on_delete=models.CASCADE)
    off_code = models.ForeignKey(to=Discount, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=9, choices=[('PAY', 'payed'), ('NPY', 'not_pay')])
    total_price = models.PositiveIntegerField()
    final_price = models.PositiveIntegerField()


class CartItem(BaseModel):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.OneToOneField(to=Product, on_delete=models.CASCADE)
    number_item = models.PositiveIntegerField()
