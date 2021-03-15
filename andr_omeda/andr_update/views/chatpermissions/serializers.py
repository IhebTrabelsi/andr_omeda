# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatPermissions
class ChatPermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatPermissions
        fields = '__all__'