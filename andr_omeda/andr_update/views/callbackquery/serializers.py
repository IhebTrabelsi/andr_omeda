# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import CallbackQuery, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()
from andr_omeda.andr_update.views.message.serializers import MessageSerializer()


class CallbackQuerySerializer(serializers.ModelSerializer):
    callback_query_from = AndruserSerializer()
    message = MessageSerializer()

    class Meta:
        model = CallbackQuery
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data.pop('from', None)
        callback_query_from = Andruser.get_user_with_id_and_first_name(user.get('user_id'), user.get('first_name'))
        try:
            message = validated_data.pop('message', None)
            if message.get('chat'):
                chat_id = message.get('chat').get('id')
                chat = Chat.objects.get(chat_id=chat_id)
                message = chat.get_message()
            else:
                message = Message.get_message_with_message_id_list(message_id=message.get('message_id'))[0]
            callback_query = CallbackQuery(**validated_data)
            callback_query.callback_query_from = user
            callback_query.messaage = message
            callback_query.save()
        except:
            raise Exception("CallbackQuery serializer Exception !!")
