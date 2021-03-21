# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ProximityAlertTriggered
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer

class ProximityAlertTriggeredSerializer(serializers.ModelSerializer):
    traveler = AndruserSerializer()
    watcher = AndruserSerializer()
    class Meta:
        model = ProximityAlertTriggered
        fields = '__all__'

    def create(self, validated_data):
        traveler_data = validated_data.pop('traveler', None)
        watcher_data = validated_data.pop('watcher', None)
        proximity_alert_triggered = ProximityAlertTriggered(**validated_data)
        if traveler_data:
            traveler_ser = self.fields['traveler']
            traveler = traveler_ser(**traveler_data)
            traveler = traveler.is_valid().save()
            proximity_alert_triggered.traveler = traveler
        if watcher_data:
            watcher_ser = self.fields['watcher']
            watcher = watcher_ser(**watcher_data)
            watcher = watcher.is_valid().save()
            proximity_alert_triggered.watcher = watcher

        return proximity_alert_triggered.save()