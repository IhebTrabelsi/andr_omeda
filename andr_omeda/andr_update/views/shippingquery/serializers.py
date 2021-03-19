# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ShippingQuery
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()
from andr_omeda.andr_update.views.shippingaddress.serializers import ShippingAddressSerializer()

class ShippingQuerySerializer(serializers.ModelSerializer):
    shipping_query_from = AndruserSerializer()
    shipping_address = ShippingAddressSerializer()
    class Meta:
        model = ShippingQuery
        fields = '__all__'

    def create(self, validated_data):
        shipping_query_from_data = validated_data.pop('from', None)
        shipping_address_data = validated_data.pop('shipping_address', None)
        shipping_query = ShippingQuery(**validated_data)
        if shipping_query_from_data:
            shipping_query_from_ser = self.fields['shipping_query_from']
            shipping_query_from = shipping_query_from_ser(**shipping_query_from_data)
            shipping_query_from = shipping_query_from.is_valid().save()
            shipping_query.shipping_query_from = shipping_query_from
        if shipping_address_data:
            shipping_address_ser = self.fields['shipping_address']
            shipping_address = shipping_address_ser(**shipping_address_data)
            shipping_address = shipping_address.is_valid().save()
            shipping_query.shipping_address = shipping_address

        return shipping_query.save()