# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import MessageEntity, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer

class MessageEntityListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        users = []
        entities = []
        for entity in validated_data:
            if entity.get('user'):
                if Andruser.user_with_id_exists(entity.get('user').get('id')):
                    users.append(Andruser.objects.get(pk=entity.pop('user').get('id')))
                else:
                    user = AndruserSerializer(**entity.pop('user')).is_valid().save()
                    users.append(user)
            entities.append(MessageEntity(**entity))
        for entity, user in zip(entities, users):
            entity.user = user 
        return entities



class MessageEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageEntity
        list_serializer_class = MessageEntityListSerializer
        fields = '__all__'