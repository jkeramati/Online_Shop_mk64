from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from costumer.models import Costumer, Address

User = get_user_model


class CostumerLoginForm(AuthenticationForm):

    help_texts = {
        'username': _("Phone"),
        'password': _("Password"),
    }

    def __init__(self, *args, **kwargs):
        super(CostumerLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.items():
            # print(field[0],field[1])
            field[1].widget.attrs['placeholder'] = self.help_texts[field[0]]


class CostumerSignUpForm(UserCreationForm):

    class Meta:
        model = Costumer
        fields = ['phone', 'password1', 'password2']

        help_texts = {
            'phone': _("Phone"),
            'password1': _("Password"),
            'password2': _("Confirm Password"),
        }

    def __init__(self, *args, **kwargs):
        super(CostumerSignUpForm, self).__init__(*args, **kwargs)
        for field in self.fields.items():
            field[1].widget.attrs['placeholder'] = self.Meta.help_texts[field[0]]


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
