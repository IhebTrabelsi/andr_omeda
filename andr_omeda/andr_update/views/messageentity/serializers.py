# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import MessageEntity, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer



class MessageEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageEntity
        fields = '__all__'

    def create(self, validated_data):
        if validated_data.get('user', None):
            validated_data.pop('user')
        
        message_entity = MessageEntity.objects.create(**validated_data)
        return message_entity

class MessageEntityListSerializer(serializers.Serializer):
    def create(self, validated_data):
        _lists = self.context['lists']
        _specials = self.context['specials']
        entity_instances = []
        for entity, user in zip(_lists['message__entities'], _specials['entities__users']):
            entity_instance_ser = MessageEntitySerializer(data=entity)
            entity_instance_is_valid = entity_instance_ser.is_valid()
            entity_instance = entity_instance_ser.save()
            if len(user) > 0:
                user_instance = Andruser.get_user_with_id(user_id=user['id'])
                if not user_instance:
                    user_instance = Andruser.objects.create(**user)
                entity_instance.user = user_instance 
            entity_instance.save()
            entity_instances.append(entity_instance)

        return entity_instances

