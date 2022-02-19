from django.db import models
from core.models import *
from costumer.models import Costumer
from product.models import *
from costumer.models import Address


# Create your models here.


class Cart(BaseModel):
    costumer = models.ForeignKey(to=Costumer, on_delete=models.RESTRICT)
    address = models.ForeignKey(to=Address, on_delete=models.RESTRICT)
    off_code = models.ForeignKey(to=OffCode, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=9, choices=[('PAY', 'payed'), ('NPY', 'not_pay')])
    total_price = models.IntegerField()
    final_price = models.IntegerField()

    class Meta:
        unique_together = [['costumer', 'off_code']]


class CartItem(BaseModel):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    number_item = models.IntegerField(default=1)
