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
    pinned_message = MessageSerializer()
    class Meta:
        model = Chat
        fields = '__all__'

    def create(self, validated_data):
        chat_id = validated_data.get('chat_id')
        if Chat.chat_with_id_exists(chat_id=chat_id):
            return Chat.objects.get(pk=chat_id)
        loc_ser = self.fields['location']
        perm_ser = self.fields['permissions']
        photo_ser = self.fields['photo']
        pinned_message_ser = self.fields['pinned_message']

        if validated_data.get('location'):
            loc = loc_ser(**validated_data.pop('location', None))
            loc = loc.is_valid().save()

        if validated_data.get('permissions'):
            perm = perm_ser(**validated_data.pop('permissions', None))
            perm = perm.is_valid().save()

        if validated_data.get('photo'):
            photo = photo_ser(**validated_data.pop('permissions', None))
            photo = photo.is_valid().save()

        if validated_data.get('pinned_message'):
            pinned_message = pinned_message_ser(**validated_data.pop('permissions', None))
            pinned_message = pinned_message.is_valid().save()
        
        chat = Chat(**validated_data)
        chat.location = loc
        chat.permissions = perm 
        chat.photo = photo 
        chat.pinned_message = pinned_message
        chat.save()
        return chat 