# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatMemberUpdated, Andruser, Chat
from andr_omeda.andr_update.views.chatmember.serializers import ChatMemberSerializer
from andr_omeda.andr_update.views.chatinvitelink.serializers import ChatInviteLinkSerializer
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
from andr_omeda.andr_update.views.message.serializers import ChatSerializer
class ChatMemberUpdatedSerializer(serializers.ModelSerializer):
    old_chat_member = ChatMemberSerializer()
    new_chat_member = ChatMemberSerializer()
    invite_link = ChatInviteLinkSerializer(required=False)
    chat = ChatSerializer(required=False)
    from_user = AndruserSerializer(required=False)
    class Meta:
        model = ChatMemberUpdated
        fields = '__all__'

    def create(self, validated_data):
        __chat, __user = None, None

        validated_data = self.context['validated_data']
        _unicity = self.context.get('unicity')
        _prefix = self.context.get('unicity_prefix')
        

        
        from_user_data = validated_data.pop('from_user', None)
        chat_data = validated_data.pop('chat', None)
        old_chat_member_data = validated_data.pop('old_chat_member', None)
        new_chat_member_data = validated_data.pop('new_chat_member', None)
        invite_link_data =  validated_data.pop('invite_link_data', None)
        
        if _unicity.get(_prefix + '__' + 'chat', None):
            __chat = Chat.get_chat_with_id(chat_id=_unicity.get(_prefix + '__' + 'chat', None))
        else:
            if chat_data:
                chat = ChatSerializer(data=chat_data)
                chat_is_valid = chat.is_valid(raise_exception=True)
                chat = chat.save()
                validated_data['chat'] = chat
        
        if _unicity.get(_prefix + '__' + 'from_user', None):
            __user = Andruser.objects.get(pk=_unicity.get(_prefix + '__' + 'from_user', None))
            
        else:
            if from_user_data:
                user = AndruserSerializer(data=from_user_data)
                user_is_valid = user.is_valid(raise_exception=True)
                user = user.save()
                validated_data['from_user'] = user
        
        

        if old_chat_member_data:
            old_chat_member = ChatMemberSerializer(data=old_chat_member_data, context={'validated_data':old_chat_member_data})
            old_chat_member_is_valid = old_chat_member.is_valid(raise_exception=True)
            old_chat_member = old_chat_member.save()
        
        if new_chat_member_data:
            new_chat_member = ChatMemberSerializer(data=new_chat_member_data, context={'validated_data':new_chat_member_data})
            new_chat_member_is_valid = new_chat_member.is_valid(raise_exception=True)
            new_chat_member = new_chat_member.save()

        if invite_link_data:
            new_chat_member_data['creator'] = validated_data['from_user']
            invite_link = ChatInviteLinkSerializer(data=invite_link_data)
            invite_link_is_valid = invite_link.is_valid(raise_exception=True)
            invite_link = invite_link.save()
            validated_data['invite_link'] = invite_link
            
        chat_member_updated = ChatMemberUpdated.objects.create(**validated_data)
        if old_chat_member_data:
            old_chat_member.old_member = chat_member_updated
            old_chat_member.save()
        if new_chat_member_data:
            new_chat_member.new_member = chat_member_updated
            new_chat_member.save()
        
        if __chat:
            chat_member_updated.chat = __chat
        
        if __user:
            chat_member_updated.from_user = __user
        
        

        return chat_member_updated


