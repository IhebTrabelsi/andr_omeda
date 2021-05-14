from rest_framework.fields import Field


class BotPendingModeratedObjectsCountField(Field):
    def __init__(self, **kwargs):
        kwargs['source'] = '*'
        kwargs['read_only'] = True
        super(BotPendingModeratedObjectsCountField, self).__init__(**kwargs)

    def to_representation(self, bot):
        return bot.count_pending_moderated_objects()
