from django.contrib.auth.models import UserManager, AbstractUser
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    phone = models.CharField(max_length=11, unique=True, validators=[
        validators.RegexValidator(regex='^(\+98|0)?9\d{9}$',
                                  message=_("Phone number must be entered in IR-Phone format."),
                                  code=_('invalid phone number'))])

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    objects = CustomUserManager()


    def save(self, *args, **kwargs):
        self.username = self.phone
        if User.objects.filter(id=self.id):
            self.set_password(self.password)
        super().save(*args, **kwargs)


class BaseManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def get_all(self):
        return super().get_queryset()

    def get_active_list(self):
        return super().get_queryset().filter(is_deleted=False, is_active=True)

    def get_deleted_list(self):
        return super().get_queryset().filter(is_deleted=True)

    def get_deactive_list(self):
        return self.get_queryset().filter(is_active=False)


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, editable=False)
    modify_time = models.DateTimeField(auto_now_add=True, editable=False)
    is_deleted = models.BooleanField(default=False, editable=False)
    is_active = models.BooleanField(default=True, editable=False)
    objects = BaseManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def undelete(self):
        self.is_delete = False
        self.save()

    def deactive(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()
