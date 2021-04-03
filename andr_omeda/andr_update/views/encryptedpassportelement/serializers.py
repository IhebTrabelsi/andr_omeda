# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import EncryptedPassportElement
from andr_omeda.andr_update.views.passportfile.serializers import PassportFileSerializer


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
        files_data = validated_data.pop('files', None)
        front_side_data = validated_data.pop('front_side', None)
        reverse_side_data = validated_data.pop('reverse_side', None)
        selfie_data = validated_data.pop('selfie', None)
        translation = validated_data.pop('translation', None)
       

        if validated_data.get('files'):
            files = PassportFileSerializer(data=files_data)
            files_is_valid = files.is_valid()
            files = files.save()
            validated_data['files'] = files

        if validated_data.get('front_side'):
            front_side = PassportFileSerializer(data=front_side_data)
            front_side_is_valid = front_side.is_valid()
            front_side = front_side.save()
            validated_data['front_side'] = files

        if validated_data.get('reverse_side'):
            reverse_side = PassportFileSerializer(data=reverse_side_data)
            reverse_side_is_valid = reverse_side.is_valid()
            reverse_side = reverse_side.save()
            validated_data['reverse_side'] = files


        if validated_data.get('selfie'):
            selfie = PassportFileSerializer(data=selfie_data)
            selfie_is_valid = selfie.is_valid()
            selfie = selfie.save()
            validated_data['selfie'] = files


        if validated_data.get('translation'):
            translation = PassportFileSerializer(data=translation)
            translation_is_valid = translation.is_valid()
            translation = translation.save()
            validated_data['translation'] = files
        
        encrypted_passport_element = EncryptedPassportElement(**validated_data)
        return encrypted_passport_element.save()