# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import InlineQuery, Andruser
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()
from andr_omeda.andr_update.views.location.serializers import LocationSerializer()

class InlineQuerySerializer(serializers.ModelSerializer):
    inline_query_from = AndruserSerializer()
    location = LocationSerializer()
    
    
    class Meta:
        model = InlineQuery
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('from')
        location_data = validated_data.pop('location', None)
        inline_query = InlineQuery(**validated_data)
        if Andruser.user_with_id_exists(user_data.get('id')):
            user = Andruser.objects.get(pk=user_data.get('id'))
            inline_query.inline_query_from = user
        else:
            user_ser = self.fields['inline_query_from']
            user = user_ser(**user_data).is_valid().save()
            inline_query.inline_query_from = user

        if location_data:
            location_ser = self.fields['location']
            location = location_ser(**location_data).is_valid().save()
            inline_query.location = location
        
        return inline_query.save()

        
