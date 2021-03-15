# automatically created
from rest_framework import serializers
from andr_omeda.andr_update.models import PollAnswer
from andr_omeda.andr_update.views.pollansweroptionsid.serializers import PollAnswerOptionsIdSerializer()

class PollAnswerSerializer(serializers.ModelSerializer):
    option_ids = PollAnswerOptionsId(many=True)
    class Meta:
        model = PollAnswer
        fields = '__all__'