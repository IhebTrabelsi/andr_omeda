# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import SuccessfulPayment
from andr_omeda.andr_update.views.orderinfo.serializers import OrderInfoSerializer

class SuccessfulPaymentSerializer(serializers.ModelSerializer):
    order_info = OrderInfoSerializer()
    class Meta:
        model = SuccessfulPayment
        fields = '__all__'

    def create(self, validated_data):
        order_info_data = validated_data.pop('order_info', None)
        
        if order_info_data:
            order_info = OrderInfoSerializer(**order_info_data)
            order_info = order_info.is_valid()
            order_info = order_info.save()
            validated_data['order_info'] = order_info

        successful_payment = SuccessfulPayment(**validated_data)
        return successful_payment.save()