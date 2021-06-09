from rest_framework import serializers
from andr_omeda.andr_moderation.views.validators import \
    moderated_object_id_exists, moderation_category_id_exists
from andr_omeda.andr_moderation.models import ModerationCategory, \
    ModeratedObjectCategoryChangedLog, ModeratedObjectDescriptionChangedLog, \
    ModeratedObjectStatusChangedLog

from andr_omeda.andr_moderation.views.moderation_categories.serializers import \
    ModerationCategorySerializer
from generic_relations.relations import GenericRelatedField
from andr_omeda.andr_update.models.chat import Chat
from andr_omeda.andr_base.serializers import *
from andr_omeda.andr_moderation.models import *
from andr_omeda.andr_bot.models.erp import BotERPOwner


class UpdateModeratedObjectSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=4096, required=False,
                                        allow_blank=False)
    moderated_object_id = serializers.UUIDField(
        validators=[moderated_object_id_exists],
        required=True,
    )
    category_id = serializers.IntegerField(
        validators=[moderation_category_id_exists],
        required=False
    )


class ApproveModeratedObjectSerializer(serializers.Serializer):
    moderated_object_id = serializers.UUIDField(
        validators=[moderated_object_id_exists],
        required=True,
    )


class ModeratedObjectSerializer(serializers.ModelSerializer):
    category = ModerationCategorySerializer()

    content_object = GenericRelatedField({
        Chat: CommonPublicChatSerializer(),
    })

    class Meta:
        model = ModeratedObject
        fields = (
            'id',
            'object_type',
            'object_id',
            'content_object',
            'verified',
            'status',
            'description',
            'category'
        )


class GetModeratedObjectLogsSerializer(serializers.Serializer):
    count = serializers.IntegerField(
        required=False,
        max_value=20
    )
    max_id = serializers.IntegerField(
        required=False,
    )
    moderated_object_id = serializers.UUIDField(
        validators=[moderated_object_id_exists],
        required=True,
    )

#################################################################################


class ModeratedObjectLogModerationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ModerationCategory
        fields = (
            'id',
            'name',
            'title',
            'description',
            'severity',
        )


class ModeratedObjectCategoryChangedLogSerializer(serializers.ModelSerializer):
    changed_from = ModeratedObjectLogModerationCategorySerializer()
    changed_to = ModeratedObjectLogModerationCategorySerializer()

    class Meta:
        model = ModeratedObjectCategoryChangedLog
        fields = (
            'id',
            'changed_from',
            'changed_to'
        )


class ModeratedObjectDescriptionChangedLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeratedObjectDescriptionChangedLog
        fields = (
            'id',
            'changed_from',
            'changed_to'
        )


class ModeratedObjectStatusChangedLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeratedObjectStatusChangedLog
        fields = (
            'id',
            'changed_from',
            'changed_to'
        )


class ModeratedObjectVerifiedChangedLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModeratedObjectVerifiedChangedLog
        fields = (
            'id',
            'changed_from',
            'changed_to'
        )


class ModeratedObjectLogActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = BotERPOwner
        fields = (
            'owner_erp_name',
            'created',
            'updated'
        )


class ModeratedObjectLogSerializer(serializers.ModelSerializer):
    actor = ModeratedObjectLogActorSerializer()

    content_object = GenericRelatedField({
        ModeratedObjectCategoryChangedLog: ModeratedObjectCategoryChangedLogSerializer(),
        ModeratedObjectDescriptionChangedLog: ModeratedObjectDescriptionChangedLogSerializer(),
        ModeratedObjectStatusChangedLog: ModeratedObjectStatusChangedLogSerializer(),
        ModeratedObjectVerifiedChangedLog: ModeratedObjectVerifiedChangedLogSerializer(),
    })

    class Meta:
        model = ModeratedObjectLog
        fields = (
            'id',
            'log_type',
            'actor',
            'content_object',
            'created'
        )
