# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Venue
from andr_omeda.andr_update.views.location.serializers import LocationSerializer

class VenueSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = Venue
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location', None)
        
        if location_data:
            location = LocationSerializer(data=location_data)
            location_is_valid = location.is_valid(raise_exception=True)
            location = location.save()
            validated_data['location'] = location

        venue = Venue(**validated_data)
        return venue.save()