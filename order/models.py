from django.db import models
from core.models import *
from costumer.models import Costumer
from product.models import *
from costumer.models import Address


# Create your models here.


class Cart(BaseModel):
    costumer = models.ForeignKey(to=Costumer, on_delete=models.RESTRICT)
    address = models.ForeignKey(to=Address, on_delete=models.RESTRICT, null=True, blank=True)
    off_code = models.ForeignKey(to=OffCode, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=9, choices=[('PAY', 'payed'), ('NPY', 'not_pay')])
    total_price = models.IntegerField(default=0)
    final_price = models.IntegerField(default=0)

    @property
    def calc_total_price(self):
        pass

    class Meta:
        unique_together = [['costumer', 'off_code']]


class CartItem(BaseModel):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    number_item = models.IntegerField(default=1)

    @property
    def total_cartitem_price(self):
        return self.product.price_after_discount*self.number_item
