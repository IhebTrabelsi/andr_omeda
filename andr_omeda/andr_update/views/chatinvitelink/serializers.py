# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatInviteLink, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
class ChatInviteLinkSerializer(serializers.ModelSerializer):
    creator = AndruserSerializer()
    class Meta:
        model = ChatInviteLink
        exclude = ['creator', 'chat_member_update']

    def create(self, validated_data):
        validated_data = self.context['validated_data']
        _unicity = self.context['unicity']
        _prefix = self.context['unicity_prefix']

        if _unicity.get(_prefix + '__creator', None):
            user_instance = Andruser.get_user_with_id(user_id=_unicity.get(_prefix + '__creator'))
        else:
            user = AndruserSerializer(**validated_data)
            user_is_valid = user.is_valid()
            user_instance = user.save()

        
        chat_invite_link = ChatInviteLink.objects.create(**validated_data)
        chat_invite_link.creator = user_instance
        return chat_invite_link