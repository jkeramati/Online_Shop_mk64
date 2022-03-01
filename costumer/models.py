from django.db import models
from core.models import *
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Costumer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)  # TODO set validator
    fist_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('costumer')
        verbose_name_plural = _('costumers')

    def __str__(self):
        return f"{self.fist_name} {self.last_name}"


class Address(BaseModel):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    main_st = models.CharField(max_length=30, null=True, blank=True)
    auxiliary_st = models.CharField(max_length=30, null=True, blank=True)
    alley = models.CharField(max_length=20, blank=True, null=True)
    No = models.CharField(max_length=10)

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

    def __str__(self):
        return f"{self.province} , {self.city}"
