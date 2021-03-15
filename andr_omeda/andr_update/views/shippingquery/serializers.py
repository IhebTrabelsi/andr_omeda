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