# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Location
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'