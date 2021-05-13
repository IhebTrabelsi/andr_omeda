from django.db import models
from rest_framework.exceptions import ValidationError
from django.db.models import Q, F, Count


class BotERPOwner(models.Model):
    owner_erp_name = models.CharField(_('owner-erp-name'), max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def owner_with_name_exists(cls, user_erp_name):
        qs = cls.objects.filter(owner_erp_name=user_erp_name)
        if not qs.exists():
            raise ValidationError({'user_erp_name': 'Name of user not registered as ERP user.'})

    @classmethod
    def get_bot_with_token_for_user_with_name(cls, name, **ser_data):
        token_owner = cls.objects.get(
            owner_erp_name=name,
            bots__token=ser_data['token']
        )

        return token_owner.bots.get()

    def get_pending_moderated_objects_bots(self, max_id):
        query = Q(erp_owner__owner_erp_name=self.owner_erp_name)
