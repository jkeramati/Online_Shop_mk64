from django.db import models
from core.models import *


# Create your models here.
class Comment(BaseModel):
    content = models.CharField(max_length=255)
