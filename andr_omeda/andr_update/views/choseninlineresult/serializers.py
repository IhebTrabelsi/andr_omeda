# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import ChosenInlineResult, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()
from andr_omeda.andr_update.views.location.serializers import LocationSerializer()

class ChosenInlineResultSerializer(serializers.ModelSerializer):
    chosen_inline_result_from = AndruserSerializer()
    location = LocationSerializer()
    class Meta:
        model = ChosenInlineResult
        fields = '__all__'

    def create(self, validated_data):
        user = Andruser.get_user_with_id(user_id= validated_data.pop('from').get('user_id'))
        if 'location' in validated_data:
            location_ser = self.fields['location']
            location = location_ser(**validated_data.pop('location'))
            location = location.is_valid()
            location = location.save()
        
        chosen_inline_result = ChosenInlineResult(**validated_data)
        chosen_inline_result.chosen_inline_result_from = user

        if 'location' in validated_data:
            chosen_inline_result.location = location
        
        return chosen_inline_result.save()