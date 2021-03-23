# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatMemberUpdated, Andruser, Chat
from andr_omeda.andr_update.views.chatmember.serializers import ChatMemberSerializer
from andr_omeda.andr_update.views.chatinvitelink.serializers import ChatInviteLinkSerializer
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.message.serializers import ChatSerializer
class ChatMemberUpdatedSerializer(serializers.ModelSerializer):
    from_user = AndruserSerializer()
    chat = ChatSerializer()
    old_chat_member = ChatMemberSerializer()
    new_chat_member = ChatMemberSerializer()
    invite_link = ChatInviteLinkSerializer()
    class Meta:
        model = ChatMemberUpdated
        fields = '__all__'

    def create(self, validated_data):
        from_user_data = validated_data.pop('from', None)
        chat_data = validated_data.pop('chat', None)
        old_chat_member_data = validated_data.pop('old_chat_member', None)
        new_chat_member_data = validated_data.pop('new_chat_member', None)
        invite_link_data =  validated_data.pop('invite_link_data', None)

        if Andruser.user_with_id_exists(user_id=from_user_data.get('id')):
            user = Andruser.objects.get(pk=from_user_data.get('id'))
            validated_data['from'] = user
        else:
            user = AndruserSerializer(data=from_user_data)
            user_is_valid = user.is_valid()
            user = user.save()
            validated_data['from'] = user
        
        if Chat.chat_with_id_exists(chat_id=chat_data.get('id')):
            chat = Chat.objects.get(pk=chat_data.get('id'))
            validated_data['chat'] = chat
        else:
            chat = ChatSerializer(data=chat_data)
            chat_is_valid = chat.is_valid()
            chat = chat.save()
            validated_data['chat'] = chat

        if old_chat_member_data:
            old_chat_member = ChatMemberSerializer(data=old_chat_member_data)
            old_chat_member_is_valid = old_chat_member.is_valid()
            old_chat_member = old_chat_member.save()
            validated_data['old_chat_member'] = old_chat_member
        
        if new_chat_member_data:
            new_chat_member = ChatMemberSerializer(data=new_chat_member_data)
            new_chat_member_is_valid = new_chat_member.is_valid()
            new_chat_member = new_chat_member.save()
            validated_data['new_chat_member'] = new_chat_member

        if invite_link_data:
            invite_link = ChatInviteLinkSerializer(data=invite_link_data)
            invite_link_is_valid = invite_link.is_valid()
            invite_link = invite_link.save()
            validated_data['invite_link'] = invite_link
        
        chat_member_updated = ChatMemberUpdated(**validated_data)
        return chat_member_updated.save()


