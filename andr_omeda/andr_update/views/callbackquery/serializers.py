# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import CallbackQuery, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.message.serializers import MessageSerializer


class CallbackQuerySerializer(serializers.ModelSerializer):
    message = MessageSerializer()

    class Meta:
        model = CallbackQuery
        fields = '__all__'

    def create(self, validated_data):
        __user = None

        validated_data = self.context['validated_data']
        _unicity = self.context.get('unicity')
        _prefix = self.context.get('unicity_prefix')

        user_data = validated_data.pop('from_user', None)
        message_data = validated_data.pop('message', None)

        if _unicity.get(_prefix + '__' + 'from_user', None):
            __user = Andruser.objects.get(pk=_unicity[_prefix + '__' + 'from_user'])
        else:
            if user_data:
                from_user = AndruserSerializer(data=user_data)
                from_user_is_valid = from_user.is_valid(raise_exception=True)
                from_user = from_user.save()
                validated_data['callback_query_from'] = from_user
        if message_data:
            message = MessageSerializer(data=message_data)
            message_is_valid = message.is_valid(raise_exception=True)
            message = message.save()
            validated_data['message'] = message
        
        callback_query = CallbackQuery(**validated_data)

        if __user:
            callback_query.callback_query_from = __user 
        callback_query.save()

        return callback_query

        
