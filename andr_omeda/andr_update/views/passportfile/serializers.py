# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PassportFile

class PassportFileListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        passport_files = PassportFile.bulk_passportfile_or_instance(validated_data)
        return passport_files

class PassportFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportFile
        list_serializer_class = PassportFileListSerializer
        fields = '__all__'