from rest_framework import serializers
from andr_omeda.andr_update.models.andrid import Andrid


class AndridSerializer(serializers.ModelSerializer):
    class Meta:
        model=Andrid
        fields=['_id']
    

    def create(self, validated_data):
        id_data = validated_data.pop('_id', None)
        return Andrid.create_andrid(_id=id_data)

    
