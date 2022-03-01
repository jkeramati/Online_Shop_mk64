from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from costumer.models import Costumer, Address
from core.models import User


class CostumerLoginForm(AuthenticationForm):
    help_texts = {
        'username': _("09XXXXXXXX"),
        'password': _("**********"),
    }

    def __init__(self, *args, **kwargs):
        super(CostumerLoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.items():
            print(field[0], field[1])
            field[1].widget.attrs['placeholder'] = self.help_texts[field[0]]
            # field[1].widget.attrs['class'] = "form-control"  # bootstrap form


class CostumerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['phone', 'password1', 'password2']

        # help_texts = {
        #     'phone': _("Number: 09XXXXXXXXX -IR Format"),
        #     'password1': _("Password"),
        #     'password2': _("Confirm Password"),
        # }

    def __init__(self, *args, **kwargs):
        super(CostumerSignUpForm, self).__init__(*args, **kwargs)
        # for field in self.fields.items():
        #     field[1].widget.attrs['placeholder'] = self.Meta.help_texts[field[0]]

    # def save(self, commit=True):
    #     user = super(CostumerSignUpForm, self).save(commit=False)
    #     phone = self.cleaned_data["phone"]
    #     user.phone = phone
    #     if commit:
    #         user.save()
    #     return user

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
