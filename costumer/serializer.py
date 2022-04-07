# felan
# from urllib import request


from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import Costumer, Address


class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costumer
        fields = '__all__'

    permission_classes = [IsAuthenticated]


# class Costumer2Serializer(serializers.HyperlinkedModelSerializer):
#     address = serializers.HyperlinkedRelatedField(many=True, view_name='address_view_list', read_only=True)
#
#     class Meta:
#         model = Costumer
#         fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

    permission_classes = [IsAuthenticated]
