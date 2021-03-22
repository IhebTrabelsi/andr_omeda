# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PreCheckoutQuery
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.orderinfo.serializers import OrderInfoSerializer

class PreCheckoutQuerySerializer(serializers.ModelSerializer):
    from_user = AndruserSerializer()
    order_info = OrderInfoSerializer()
    class Meta:
        model = PreCheckoutQuery
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('from')
        order_info_data = validated_data.pop('order_info', None)
        
        if Andruser.user_with_id_exists(user_id=user_data.get('id')):
            user = Andruser.objects.get(pk=user_data.get('id'))
            validated_data['from_user'] = user
        else:
            user = AndruserSerializer(**user_data)
            user = user.is_valid()
            user = user.save()
            validated_data['from_user'] = user

        if order_info_data:
            order_info_ser = self.fields['order_info']
            order_info = OrderInfoSerializer(**order_info_data)
            order_info = order_info.is_valid()
            order_info = order_info.save()
            validated_data['order_info'] = order_info

        pre_checkout_query = PreCheckoutQuery(**validated_data)
        return pre_checkout_query.save()