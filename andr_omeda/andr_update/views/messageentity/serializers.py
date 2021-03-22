# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import MessageEntity, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer

class MessageEntityListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        entities = []
        for entity in validated_data:
            if entity.get('user'):
                if Andruser.user_with_id_exists(entity.get('user').get('id')):
                    user = Andruser.objects.get(pk=entity.pop('user').get('id'))
                    entity['user'] = user
                else:
                    user = AndruserSerializer(**entity.pop('user'))
                    user = user.is_valid()
                    user = user.save()
                    entity['user'] = user
            entities.append(MessageEntity(**entity))
        
        return MessageEntity.objects.bulk_create(entities)



class MessageEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageEntity
        list_serializer_class = MessageEntityListSerializer
        fields = '__all__'