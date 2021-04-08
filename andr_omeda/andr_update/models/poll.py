from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from andr_omeda.andr_update.models import Message, Update


class Poll(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name="poll",
        blank=True,
        null=True
    )
    update = models.OneToOneField(
        Update,
        on_delete=models.CASCADE,
        related_name="poll",
        blank=True,
        null=True
    )
    poll_id = models.TextField(_("poll_id"), blank=True, null=True)
    question = models.CharField(_("question"), max_length=300, blank=False)
    total_voter_count = models.IntegerField(_("total_voter_count"), blank=False, null=True)
    is_closed = models.BooleanField(_("is_closed"), blank=False, null=True)
    is_anonymous = models.BooleanField(_("is_anonymous"), blank=False, null=True)
    type = models.TextField(_("type"), blank=False)
    allows_multiple_answers = models.BooleanField(_("allows_multiple_answers"), blank=False, null=True)
    correct_option_id = models.IntegerField(_("correct_option_id"), blank=True, null=True)
    explanation = models.CharField(_("explanation"), max_length=100, blank=True)
    open_period = models.IntegerField(_("open_period"), blank=True, null=True)
    close_date = models.IntegerField(_("close_date"), blank=True, null=True)

    @classmethod
    def poll_id_sanitize(cls, data, *args, **kwargs):
        if data.get('poll', None):
            data['poll']['poll_id'] = data['poll']['id']
            del data['poll']['id']
        return data

    @classmethod
    def extract_lists(cls, data, lists, *args, **kwargs):
        if data.get('poll', None):
            options = data['poll'].get('options', None)
            if not options == None:
                if len(options) == 0:
                    del data['poll']['options']
                else:
                    lists['poll__options'] = data['poll']['options']
                    del data['poll']['options']
            entities = data['poll'].get('explanation_entities', None)
            if not entities == None:
                if len(entities) == 0:
                    print("\n\n YES explanation_entities EXISTS !!! \n\n")
                    del data['poll']['explanation_entities']
                else:
                    print("\n\n YES explanation_entities EXISTS !!! \n\n")
                    lists['poll__explanation_entities'] = data['poll']['explanation_entities']
                    del data['poll']['explanation_entities']
            
            
        return lists