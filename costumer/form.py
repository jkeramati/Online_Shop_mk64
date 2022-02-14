from django.forms import ModelForm

from costumer.models import Costumer, Address


class CostumerForm(ModelForm):
    class Meta:
        model = Costumer
        fields = "__all__"


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
