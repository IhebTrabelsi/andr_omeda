# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import Poll
from andr_omeda.andr_update.views.polloption.serializers import PollOptionSerializer()

class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(many=True)
    class Meta:
        model = Poll
        fields = '__all__'