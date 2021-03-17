# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatMemberUpdated
from andr_omeda.andr_update.views.chatmember.serializers import ChatMemberSerializer
from andr_omeda.andr_update.views.chatinvitelink.serializers import ChatInviteLinkSerializer
class ChatMemberUpdatedSerializer(serializers.ModelSerializer):
    old_chat_member = ChatMemberSerializer()
    new_chat_member = ChatMemberSerializer()
    invite_link = ChatInviteLinkSerializer()
    class Meta:
        model = ChatMemberUpdated
        fields = '__all__'

    def create(self, validated_data):
        chat_id = validated_data.pop('chat').get('chat_id')
        user_id = validated_data.pop('from').get('chat_id')
        chat = Chat.get_chat_with_id(chat_id=chat_id)
        user = Andruser.get_user_with_id(user_id=user_id)

        old_chat_member_ser = self.fields['old_chat_member'] 
        old_chat_member = old_chat_member_ser(**validated_data.pop('old_chat_member'))
        old_chat_member = old_chat_member.is_valid()
        old_chat_member = old_chat_member.save()

        new_chat_member_ser = self.fields['new_chat_member'] 
        new_chat_member = new_chat_member_ser(**validated_data.pop('new_chat_member'))
        new_chat_member = new_chat_member.is_valid()
        new_chat_member = new_chat_member.save()

        invite_link_ser = self.fields['invite_link']
        invite_link = invite_link_ser(**validated_data.pop('invite_link'))
        invite_link = invite_link.is_valid()
        invite_link = invite_link.save()

        chat_member_updated = ChatMemberUpdated(**validated_data)
        chat_member_updated.chat = chat 
        chat_member_updated.user = user 
        chat_member_updated.old_chat_member = old_chat_member
        chat_member_updated.new_chat_member = new_chat_member
        chat_member_updated.invite_link = invite_link

        chat_member_updated.save()


