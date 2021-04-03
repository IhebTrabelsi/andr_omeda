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
        traveler_data = validated_data.pop('traveler')
        watcher_data = validated_data.pop('watcher')
        
        if Andruser.user_with_id_exists(user_id=traveler_data.get('id')):
            traveler = Andruser.objects.get(pk=traveler_data.get('id'))
            validated_data['traveler'] = traveler
        else:
            traveler = AndruserSerializer(data=traveler_data)
            traveler_is_valid = traveler.is_valid()
            traveler = traveler.save()
            validated_data['traveler'] = traveler

        if Andruser.user_with_id_exists(user_id=watcher_data.get('id')):
            watcher = Andruser.objects.get(pk=watcher_data.get('id'))
            validated_data['watcher'] = watcher
        else:
            watcher = AndruserSerializer(data=watcher_data)
            watcher_is_valid = watcher.is_valid()
            watcher = watcher.save()
            validated_data['watcher'] = watcher

        proximity_alert_triggered = ProximityAlertTriggered(**validated_data)
        return proximity_alert_triggered.save()