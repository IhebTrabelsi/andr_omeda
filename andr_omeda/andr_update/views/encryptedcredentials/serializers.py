# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import EncryptedCredentials
class EncryptedCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncryptedCredentials
        fields = '__all__'