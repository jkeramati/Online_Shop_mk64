from django.db import models
from core.models import *


# Create your models here.

class Costumer(BaseModel):
    name = models.CharField(max_length=50)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    email = models.EmailField()


class Address(BaseModel):
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    other = models.CharField(max_length=80)
