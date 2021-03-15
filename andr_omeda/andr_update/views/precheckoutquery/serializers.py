# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PreCheckoutQuery
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()
from andr_omeda.andr_update.views.orderinfo.serializers import OrderInfoSerializer()

class PreCheckoutQuerySerializer(serializers.ModelSerializer):
    pre_checkout_query_from = AndruserSerializer()
    order_info = OrderInfoSerializer()
    class Meta:
        model = PreCheckoutQuery
        fields = '__all__'