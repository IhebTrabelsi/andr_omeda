# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Venue
from andr_omeda.andr_update.views.location.serializers import LocationSerializer()

class VenueSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = Venue
        fields = '__all__'