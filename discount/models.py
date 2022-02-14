from django.db import models
from core.models import *


# Create your models here.
class Discount(BaseModel):
    code = models.CharField(max_length=10, null=True, blank=True)
    type_disc = models.BooleanField(null=True, blank=True)
    value = models.FloatField()
