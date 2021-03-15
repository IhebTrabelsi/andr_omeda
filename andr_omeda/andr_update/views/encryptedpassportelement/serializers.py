# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import EncryptedPassportElement
from andr_omeda.andr_update.views.passportfile.serializers import PassportFileSerializer()


class EncryptedPassportElementSerializer(serializers.ModelSerializer):
    files = PassportFileSerializer(many=True)
    front_side = PassportFileSerializer()
    reverse_side = PassportFileSerializer()
    selfie = PassportFileSerializer()
    translation = PassportFileSerializer(many=True)
    class Meta:
        model = EncryptedPassportElement
        fields = '__all__'