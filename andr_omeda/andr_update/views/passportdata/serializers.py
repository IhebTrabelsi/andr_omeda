# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PassportData
from andr_omeda.andr_update.views.encryptedcredentials.serializers import EncryptedCredentialsSerializer
from andr_omeda.andr_update.views.encryptedpassportelement.serializers import EncryptedPassportElementSerializer

class PassportDataSerializer(serializers.ModelSerializer):
    credentials = EncryptedCredentialsSerializer()
    data = EncryptedPassportElementSerializer(many=True)
    class Meta:
        model = PassportData
        fields = '__all__'

    def create(self, validated_data):
        credentials_data = validated_data.pop('credentials', None)
        data_data = validated_data.pop('data', None)
        
        if credentials_data:
            credentials = EncryptedCredentialsSerializer(**credentials_data)
            credentials = credentials.is_valid()
            credentials = credentials.save()
            validated_data['credentials'] = credentials
        if data_data:
            data = EncryptedPassportElementSerializer(**data_data)
            data = data.is_valid()
            data = data.save()
            validated_data['data'] = data
        
        passport_data = PassportData(**validated_data)
        return passport_data.save()
