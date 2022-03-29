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
    image = models.FileField(null=True, default=None, blank=True, upload_to='product/')
    stock = models.IntegerField(default=1)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return f"{self.name} with {self.price}$ and {self.category} category"

    @property
    def price_after_discount(self):
        if self.discount:
            return self.discount.discounted_price(int(self.price))
        else:
            return self.price

    @property
    def url_image_set(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Category(BaseModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.FileField(null=True, blank=True, upload_to='category/')

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return f"{self.name}"

    @property
    def url_image_set(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Brand(BaseModel):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20, null=True, blank=True)
    image = models.FileField(null=True, blank=None, upload_to='brand/')

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

    def discounted_price(self, price: int) -> int:
        """
        Calculate the price after discount
        :param price: product price
        :return: discounted price
        """
        if self.type_disc == 'PRI':
            if price < self.value * 2:
                # More discount than price
                return price
            return int(price - int(self.value))
        elif self.type_disc == "PER":
            return price - int((self.value / 100) * price)


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
