# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ShippingQuery
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.shippingaddress.serializers import ShippingAddressSerializer

class ShippingQuerySerializer(serializers.ModelSerializer):
    shipping_address = ShippingAddressSerializer()
    class Meta:
        model = ShippingQuery
        fields = '__all__'

    def create(self, validated_data):
        __user = None

        validated_data = self.context['validated_data']
        _unicity = self.context.get('unicity')
        _prefix = self.context.get('unicity_prefix')

        user_data = validated_data.pop('from_user', None)
        shipping_address_data = validated_data.pop('shipping_address', None)

        
        if _unicity.get(_prefix + '__' + 'from_user', None):
            __user = Andruser.objects.get(pk=_unicity[_prefix + '__' + 'from_user'])
        else:
            if user_data:
                from_user = AndruserSerializer(data=user_data)
                from_user_is_valid = from_user.is_valid(raise_exception=True)
                from_user = from_user.save()
                validated_data['shipping_query_from'] = from_user

        if shipping_address_data:
            shipping_address = ShippingAddressSerializer(data=shipping_address_data)
            shipping_address_is_valid = shipping_address.is_valid(raise_exception=True)
            shipping_address = shipping_address.save()
            validated_data['shipping_address'] = shipping_address

        shipping_query = ShippingQuery(**validated_data)

        if __user:
            shipping_query.shipping_query_from = __user 
        shipping_query.save()
        
        return shipping_query