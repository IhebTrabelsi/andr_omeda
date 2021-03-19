# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatLocation, Location
from andr_omeda.andr_update.views.location.serializers import LocationSerializer()
class ChatLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = ChatLocation
        fields = '__all__'

    def create(self, validated_data):
        loc_ser = self.fields['location']
        loc = loc_ser(**validated_data.pop('location', None)).is_valid().save()
        chat_location = ChatLocation(**validated_data)
        chat_location.location = loc
        chat_location.save()
        return chat_location

