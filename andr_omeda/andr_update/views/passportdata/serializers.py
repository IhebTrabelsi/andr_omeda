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
        passport_data = PassportData(**validated_data)
        if credentials_data:
            credentials_ser = self.fields['credentials']
            credentials = credentials_ser(**credentials_data)
            credentials = credentials.is_valid().save()
            passport_data.credentials = credentials
        if data_data:
            data_ser = self.fields['data']
            data = data_ser(**data_data)
            data = data.is_valid().save()
            passport_data.data = data
        
        return passport_data.save()
