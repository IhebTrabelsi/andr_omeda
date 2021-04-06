# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import MessageEntity, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer



class MessageEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageEntity
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user', None)
        message_entity = MessageEntity(**validated_data)
        if user_data:
            if Andruser.user_with_id_exists(validated_data.get('user').get('id')):
                user = Andruser.objects.get(pk=validated_data.pop('user').get('id'))
            else:
                user = AndruserSerializer(data=validated_data.pop('user'))
                user_is_valid = user.is_valid(raise_exception=True)
                user = user.save()
            message_entity.user = user 
        return message_entity.save()
        