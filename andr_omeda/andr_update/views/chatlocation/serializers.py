# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChatLocation
from andr_omeda.andr_update.views.location.serializers import LocationSerializer()
class ChatLocationSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = ChatLocation
        fields = '__all__'