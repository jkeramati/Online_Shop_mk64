from django.db import models
from core.models import *


# Create your models here.
class Discount(BaseModel):
    type_disc = models.CharField(max_length=7, choices=[('PRI', 'price'), ('PER', 'percent')])
    value = models.IntegerField()

    def profit(self, val: int):
        if self.type_disc == 'price':
            if val >= 2 * self.value:
                return self.value
            else:
                return 0
        elif self.type_disc == 'percent':
            return (val * self.value) / 100


class OffCode(Discount):
    code = models.CharField(max_length=10, null=True, blank=True)
