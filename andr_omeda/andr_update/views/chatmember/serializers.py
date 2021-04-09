# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatMember, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
class ChatMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMember
        exclude = ['old_member', 'new_member', 'user']

    def create(self, validated_data):
        validated_data = self.context['validated_data']
        _unicity = self.context['unicity']
        _prefix = self.context['unicity_prefix']

        if _unicity.get(_prefix + '__user', None):
            user_instance = Andruser.get_user_with_id(user_id=_unicity.get(_prefix + '__user'))
        else:
            user = AndruserSerializer(**validated_data)
            user_is_valid = user.is_valid()
            user_instance = user.save()

        
        chat_member = ChatMember.objects.create(**validated_data)
        chat_member.user = user_instance
        return chat_member