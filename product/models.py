from django.db import models

from core.models import *
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Product(BaseModel):
    name = models.CharField(max_length=50)  # TODO set validator
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.FileField(null=True, default=None, blank=None, upload_to='product/')

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return f"{self.name} with {self.price}$ and {self.category} category"


class Category(BaseModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.FileField(null=True, default=None, blank=None, upload_to='category/')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return f"{self.name}"


class Brand(BaseModel):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20, null=True, blank=True)
    image = models.FileField(null=True, default=None, blank=None, upload_to='brand/')

    def __str__(self):
        return f"{self.name}"


class BaseDiscount(BaseModel):
    type_disc = models.CharField(max_length=7, choices=[('PRI', 'price'), ('PER', 'percent')])
    value = models.IntegerField()

    def __str__(self):
        return f"type of discount: {self.type_disc} with {self.value} value"

    def profit(self, val: int):
        if self.type_disc == 'price':
            if val >= 2 * self.value:
                return self.value
            else:
                return 0
        elif self.type_disc == 'percent':
            return (val * self.value) / 100

    class Meta:
        abstract = True


class Discount(BaseDiscount):
    pass

    class Meta:
        verbose_name = _('discount')
        verbose_name_plural = _('discounts')


class OffCode(BaseDiscount):
    code = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        verbose_name = _('off code')
        verbose_name_plural = _('off codes')

# class Contact(models.Model):
#     name = models.CharField(max_length=40)
#     phone = models.CharField(max_length=13)
#     email = models.EmailField()
#     message = models.TextField()
