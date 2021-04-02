# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatMember
class ChatMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMember
        exclude = ['old_member', 'new_member', 'user']

    def create(self, validated_data):
        user = validated_data.pop('user', None)
        chat_member = ChatMember(**validated_data)
        if user:
            chat_member.user = user
        return chat_member.save()