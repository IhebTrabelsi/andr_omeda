# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PreCheckoutQuery
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.orderinfo.serializers import OrderInfoSerializer

class PreCheckoutQuerySerializer(serializers.ModelSerializer):
    pre_checkout_query_from = AndruserSerializer()
    order_info = OrderInfoSerializer()
    class Meta:
        model = PreCheckoutQuery
        fields = '__all__'

    def create(self, validated_data):
        pre_checkout_query_from_data = validated_data.pop('from', None)
        order_info_data = validated_data.pop('order_info', None)
        pre_checkout_query = PreCheckoutQuery(**validated_data)
        if pre_checkout_query_from_data:
            pre_checkout_query_from_ser = self.fields['pre_checkout_query_from']
            pre_checkout_query_from = pre_checkout_query_from_ser(**pre_checkout_query_from_data)
            pre_checkout_query_from = pre_checkout_query_from.is_valid().save()
            pre_checkout_query.pre_checkout_query_from = pre_checkout_query_from
        if order_info_data:
            order_info_ser = self.fields['order_info']
            order_info = order_info_ser(**order_info_data)
            order_info = order_info.is_valid().save()
            pre_checkout_query.order_info = order_info

        return pre_checkout_query.save()