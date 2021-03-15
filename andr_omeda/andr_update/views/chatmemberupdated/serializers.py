# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatMemberUpdated
from andr_omeda.andr_update.views.chatmember.serializers import ChatMemberSerializer()
class ChatMemberUpdatedSerializer(serializers.ModelSerializer):
    old_chat_member = ChatMemberSerializer()
    new_member = ChatMemberSerializer()
    class Meta:
        model = ChatMemberUpdated
        fields = '__all__'