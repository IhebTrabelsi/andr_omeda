# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Andruser




class AndruserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Andruser
        fields='__all__'
        extra_kwargs = {
            'user_id': {'validators': []},
        }

    def create(self, validated_data):
            
        if Andruser.user_with_id_exists(validated_data.get('user_id')):
            user = Andruser.objects.get(pk=validated_data.get('user_id'))
        else:
            user = Andruser.objects.create(**validated_data)
        
        return user
