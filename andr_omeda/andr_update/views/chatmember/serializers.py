# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatMember
class ChatMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMember
        fields = '__all__'