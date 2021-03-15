# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ProximityAlertTriggered
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()

class ProximityAlertTriggeredSerializer(serializers.ModelSerializer):
    traveler = AndruserSerializer()
    watcher = AndruserSerializer()
    class Meta:
        model = ProximityAlertTriggered
        fields = '__all__'