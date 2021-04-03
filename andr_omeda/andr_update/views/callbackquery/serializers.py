# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import CallbackQuery, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.message.serializers import MessageSerializer


class CallbackQuerySerializer(serializers.ModelSerializer):
    callback_query_from = AndruserSerializer()
    message = MessageSerializer()

    class Meta:
        model = CallbackQuery
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('from', None)
        message_data = validated_data.pop('message', None)
        if Andruser.user_with_id_exists(user_id=user_data.get('id')):
            user = Andruser.objects.get(pk=user_data.get('id'))
            validated_data['callback_query_from'] = user
        else:
            user = AndruserSerializer(data=user_data)
            user_is_valid = user.is_valid()
            user = user.save()
            validated_data['callback_query_from'] = user
        if message_data:
            message = MessageSerializer(data=message_data)
            message_is_valid = message.is_valid()
            message = message.save()
            validated_data['message'] = message
        
        callback_query = CallbackQuery(**validated_data)
        return callback_query.save()

        
