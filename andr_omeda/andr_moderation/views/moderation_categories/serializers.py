from rest_framework import serializers

from andr_omeda.andr_moderation.models import ModerationCategory


class ModerationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModerationCategory

        fields = (
            'id',
            'name',
            'title',
            'severity',
            'description',
        )
