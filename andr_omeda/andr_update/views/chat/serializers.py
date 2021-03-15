# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Chat
from andr_omeda.andr_update.views.chatlocation.serializers import ChatLocationSerializer()
from andr_omeda.andr_update.views.chatpermissions.serializers import ChatPermissionsSerializer()
from andr_omeda.andr_update.views.chatphoto.serializers import ChatPhotoSerializer()
from andr_omeda.andr_update.views.message.serializers import MessageSerializer()

class ChatSerializer(serializers.ModelSerializer):
    location = ChatLocationSerializer()
    permissions = ChatPermissionsSerializer()
    photo = ChatPhotoSerializer()
    pinned_message = MessageSerializer()
    class Meta:
        model = Chat
        fields = '__all__'