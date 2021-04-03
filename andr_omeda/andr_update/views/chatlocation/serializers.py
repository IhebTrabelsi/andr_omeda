# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatLocation, Location
from andr_omeda.andr_update.views.location.serializers import LocationSerializer
class ChatLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = ChatLocation
        fields = '__all__'

    def create(self, validated_data):
        loc_data = validated_data.pop('location', None)
        if loc_data:
            loc = LocationSerializer(data=loc_data)
            loc_is_valid = loc.is_valid()
            loc = loc.save()
            validated_data['location'] = loc
        
        chat_location = ChatLocation(**validated_data)
        return chat_location.save()
        

