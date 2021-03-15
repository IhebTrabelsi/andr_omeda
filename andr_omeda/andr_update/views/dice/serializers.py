# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Dice
class DiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dice
        fields = '__all__'