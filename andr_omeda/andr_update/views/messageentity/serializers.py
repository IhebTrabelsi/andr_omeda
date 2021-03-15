# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import MessageEntity
class MessageEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageEntity
        fields = '__all__'