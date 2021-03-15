# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import CallbackQuery
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()
from andr_omeda.andr_update.views.message.serializers import MessageSerializer()

class CallbackQuerySerializer(serializers.ModelSerializer):
    callback_query_from = AndruserSerializer()
    message = MessageSerializer()
    class Meta:
        model = CallbackQuery
        fields = '__all__'