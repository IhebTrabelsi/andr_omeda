# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PollOption
class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = '__all__'