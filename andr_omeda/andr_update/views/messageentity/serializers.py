# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import MessageEntity, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer



class MessageEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageEntity
        fields = '__all__'

    def create(self, validated_data):
        print("xXx"*15)
        print(validated_data)
        user_data = validated_data.pop('user', None)
        message_entity = MessageEntity(**validated_data)
        print(message_entity)
        if user_data:
            if Andruser.user_with_id_exists(validated_data.get('user').get('id')):
                user = Andruser.objects.get(pk=validated_data.pop('user').get('id'))
            else:
                user = AndruserSerializer(data=validated_data.pop('user'))
                user_is_valid = user.is_valid()
                user = user.save()
            message_entity.user = user 
        print("|")
        print("|")
        print("|")
        print(message_entity.save())
        return message_entity.save()
        