# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import SuccessfulPayment
from andr_omeda.andr_update.views.orderinfo.serializers import OrderInfoSerializer()

class SuccessfulPaymentSerializer(serializers.ModelSerializer):
    order_info = OrderInfoSerializer()
    class Meta:
        model = SuccessfulPayment
        fields = '__all__'