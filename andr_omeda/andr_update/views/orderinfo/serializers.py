# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import OrderInfo
from andr_omeda.andr_update.views.shippingaddress.serializers import ShippingAddressSerializer()

class OrderInfoSerializer(serializers.ModelSerializer):
    shipping_address = ShippingAddress()
    class Meta:
        model = OrderInfo
        fields = '__all__'

    def create(self, validated_data):
        shipping_address_data = validated_data.pop('shipping_address', None)
        order_info = OrderInfo(**validated_data)
        if shipping_address_data:
            shipping_address_ser = self.fields['shipping_address']
            shipping_address = shipping_address_ser(**shipping_address_data)
            shipping_address = shipping_address.is_valid().save()
            order_info.shipping_address = shipping_address
        return order_info.save()