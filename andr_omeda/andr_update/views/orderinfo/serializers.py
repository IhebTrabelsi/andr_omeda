# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import OrderInfo
from andr_omeda.andr_update.views.shippingaddress.serializers import ShippingAddressSerializer()

class OrderInfoSerializer(serializers.ModelSerializer):
    shipping_address = ShippingAddress()
    class Meta:
        model = OrderInfo
        fields = '__all__'