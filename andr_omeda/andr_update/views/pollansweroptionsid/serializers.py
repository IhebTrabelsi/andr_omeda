# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PollAnswerOptionsId
class PollAnswerOptionsIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollAnswerOptionsId
        fields = '__all__'