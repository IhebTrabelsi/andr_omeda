# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import OrderInfo
from andr_omeda.andr_update.views.shippingaddress.serializers import ShippingAddressSerializer

class OrderInfoSerializer(serializers.ModelSerializer):
    shipping_address = ShippingAddressSerializer()
    class Meta:
        model = OrderInfo
        fields = '__all__'

    def create(self, validated_data):
        shipping_address_data = validated_data.pop('shipping_address', None)
        
        if shipping_address_data:
            shipping_address = ShippingAddressSerializer(**shipping_address_data)
            shipping_address = shipping_address.is_valid()
            shipping_address = shipping_address.save()
            validated_data['shipping_address'] = shipping_address
        
        order_info = OrderInfo(**validated_data)
        return order_info.save()