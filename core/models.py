from django.db import models

# Create your models here.
class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)

    def get_all(self):
        return super().get_queryset()


class BaseModel(models.Model):
    objects = BaseManager()
    create_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    modify_datetime = models.DateTimeField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True, editable=False)
    is_delete = models.BooleanField(default=False, editable=False)

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_delete = True
        self.save()

    def undelete(self):
        self.is_delete = False
        self.save()

    def active(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()