# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PassportData
from andr_omeda.andr_update.views.encryptedcredentials.serializers import EncryptedCredentialsSerializer()
from andr_omeda.andr_update.views.encryptedpassportelement.serializers import EncryptedPassportElementSerializer()

class PassportDataSerializer(serializers.ModelSerializer):
    credentials = EncryptedCredentialsSerializer()
    data = EncryptedPassportElementSerializer()
    class Meta:
        model = PassportData
        fields = '__all__'