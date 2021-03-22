# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ShippingQuery
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.shippingaddress.serializers import ShippingAddressSerializer

class ShippingQuerySerializer(serializers.ModelSerializer):
    shipping_query_from = AndruserSerializer()
    shipping_address = ShippingAddressSerializer()
    class Meta:
        model = ShippingQuery
        fields = '__all__'

    def create(self, validated_data):
        shipping_query_from_data = validated_data.pop('from', None)
        shipping_address_data = validated_data.pop('shipping_address', None)

        
        if Andruser.user_with_id_exists(user_id=shipping_query_from_data.get('id')):
            user = Andruser.objects.get(pk=shipping_query_from_data.get('id'))
            validated_data['shipping_query_from'] = user
        else:
            user = AndruserSerializer(**shipping_query_from_data)
            user = user.is_valid()
            user = user.save()
            validated_data['shipping_query_from'] = user

        if shipping_address_data:
            shipping_address = ShippingAddressSerializer(**shipping_address_data)
            shipping_address = shipping_address.is_valid()
            shipping_address = shipping_address.save()
            validated_data['shipping_address'] = shipping_address

        shipping_query = ShippingQuery(**validated_data)
        return shipping_query.save()