from django.db import models
from core.models import *


# Create your models here.
class Discount(BaseModel):
    type_disc = models.CharField(max_length=7, choices=[('PRI', 'price'), ('PER', 'percent')])
    value = models.IntegerField()
