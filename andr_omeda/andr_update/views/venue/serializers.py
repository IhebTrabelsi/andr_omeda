# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Venue
from andr_omeda.andr_update.views.location.serializers import LocationSerializer()

class VenueSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = Venue
        fields = '__all__'

    def create(self, validated_data):
        location_data = validated_data.pop('location', None)
        venue = Venue(**validated_data)
        if location_data:
            location_ser = self.field['location']
            location = location_ser(**location_data)
            location = location.is_valid().save()
            venue.location = location 

        return venue.save()