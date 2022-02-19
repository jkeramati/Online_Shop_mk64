from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from costumer.models import Costumer, Address


class CostumerForm(ModelForm):
    class Meta:
        model = Costumer
        fields = "__all__"
        labels = {
            'address': _('Address')
        }


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
