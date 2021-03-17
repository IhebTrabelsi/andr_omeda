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
    
    def create(self, validated_data):
        if validated_data.get('files'):
            files_ser = self.fields['files']
            files = files_ser(**validated_data.pop('files'))
            files = files.is_valid()
            files = files.save()
        if validated_data.get('front_side'):
            front_side_ser = self.fields['front_side']
            front_side = front_side_ser(**validated_data.pop('front_side'))
            front_side = front_side.is_valid()
            front_side = front_side.save()
        if validated_data.get('reverse_side'):
            reverse_side_ser = self.fields['reverse_side']
            reverse_side = reverse_side_ser(**validated_data.pop('reverse_side'))
            reverse_side = reverse_side.is_valid()
            reverse_side = reverse_side.save()
        if validated_data.get('selfie'):
            selfie_ser = self.fields['selfie']
            selfie = selfie_ser(**validated_data.pop('selfie'))
            selfie = selfie.is_valid()
            selfie = selfie.save()
        if validated_data.get('translation'):
            translation_ser = self.fields['translation']
            translation = translation_ser(**validated_data.pop('translation'))
            translation = translation.is_valid()
            translation = translation.save()
        
        encrypted_passport_element = EncryptedPassportElement(**validated_data)

        if validated_data.get('files'):
            encrypted_passport_element.files = files
        if validated_data.get('front_side'):
            encrypted_passport_element.front_side = front_side
        if validated_data.get('reverse_side'):
            encrypted_passport_element.reverse_side = reverse_side
        if validated_data.get('selfie'):
            encrypted_passport_element.selfie = selfie
        if validated_data.get('translation'):
            encrypted_passport_element.translation = translation
        
        return encrypted_passport_element.save()