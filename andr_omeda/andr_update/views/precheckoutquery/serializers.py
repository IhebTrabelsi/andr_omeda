# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PreCheckoutQuery
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.orderinfo.serializers import OrderInfoSerializer

class PreCheckoutQuerySerializer(serializers.ModelSerializer):
    order_info = OrderInfoSerializer()
    class Meta:
        model = PreCheckoutQuery
        fields = '__all__'

    def create(self, validated_data):
        __user = None

        validated_data = self.context['validated_data']
        _unicity = self.context.get('unicity')
        _prefix = self.context.get('unicity_prefix')

        user_data = validated_data.pop('from_user', None)
        order_info_data = validated_data.pop('order_info', None)
        
        if _unicity.get(_prefix + '__' + 'from_user', None):
            __user = Andruser.objects.get(pk=_unicity[_prefix + '__' + 'from_user'])
        else:
            if user_data:
                from_user = AndruserSerializer(data=user_data)
                from_user_is_valid = from_user.is_valid(raise_exception=True)
                from_user = from_user.save()
                validated_data['from_user'] = from_user

        if order_info_data:
            order_info_ser = self.fields['order_info']
            order_info = OrderInfoSerializer(data=order_info_data)
            order_info_is_valid = order_info.is_valid(raise_exception=True)
            order_info = order_info.save()
            validated_data['order_info'] = order_info

        pre_checkout_query = PreCheckoutQuery(**validated_data)

        if __user:
            pre_checkout_query.from_user = __user 
        pre_checkout_query.save()

        return pre_checkout_query.save()