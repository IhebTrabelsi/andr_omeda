# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import MaskPosition
class MaskPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaskPosition
        fields = '__all__'