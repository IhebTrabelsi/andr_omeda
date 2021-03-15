# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ShippingAddress

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'