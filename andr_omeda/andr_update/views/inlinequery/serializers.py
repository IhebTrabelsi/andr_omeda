# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import InlineQuery
from andr_omeda.andr_update.views.andruser.serializers import AndruserSerializer()
from andr_omeda.andr_update.views.location.serializers import LocationSerializer()

class InlineQuerySerializer(serializers.ModelSerializer):
    inline_query_from = AndruserSerializer()
    location = LocationSerializer()
    
    
    class Meta:
        model = InlineQuery
        fields = '__all__'
