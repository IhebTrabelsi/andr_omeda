# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatMember, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer
class ChatMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMember
        exclude = ['old_member', 'new_member', 'user']

    def create(self, validated_data):
        validated_data= self.context['validated_data']
        user_data = validated_data.pop('user', None)
        if user_data:
            if Andruser.user_with_id_exists(user_id=user_data.get('user_id')):
                user = Andruser.objects.get(pk=user_data.get('user_id'))
                validated_data['user'] = user
            else:
                user = AndruserSerializer(data=user_data)
                user_is_valid = user.is_valid(raise_exception=True)
                user = user.save()
                validated_data['user'] = user
        chat_member = ChatMember(**validated_data)
        return chat_member.save()