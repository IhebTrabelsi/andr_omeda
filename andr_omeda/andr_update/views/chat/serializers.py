# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Chat
from andr_omeda.andr_update.views.chatlocation.serializers import ChatLocationSerializer
from andr_omeda.andr_update.views.chatpermissions.serializers import ChatPermissionsSerializer
from andr_omeda.andr_update.views.chatphoto.serializers import ChatPhotoSerializer
from andr_omeda.andr_update.views.message.serializers import MessageSerializer

class ChatSerializer(serializers.ModelSerializer):
    location = ChatLocationSerializer()
    permissions = ChatPermissionsSerializer()
    photo = ChatPhotoSerializer()
    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        chat_id_data = validated_data.pop('chat_id', None)
        location_data = validated_data.pop('location', None)
        permissions_data = validated_data.pop('permissions', None)
        photo_data = validated_data.pop('photo', None)

        if Chat.chat_with_id_exists(chat_id=chat_id_data):
            return Chat.objects.get(pk=chat_id_data)
        else:
            if chat_id_data:
                validated_data['id'] = chat_id_data
        
        if location_data:
            loc_ser = self.fields['location']
            loc = loc_ser(**location_data)
            loc = loc.is_valid().save()
            validated_data['location'] = loc

        if permissions_data:
            perm_ser = self.fields['permissions']
            perm = perm_ser(**permissions_data)
            perm = perm.is_valid().save()
            validated_data['permissions'] = perm

        if photo_data:
            photo_ser = self.fields['photo']
            photo = photo_ser(**photo_data)
            photo = photo.is_valid().save()
            validated_data['photo'] = photo

        
        chat = Chat(**validated_data)
        
        return chat.save()