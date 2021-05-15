from django.db import models
from rest_framework.exceptions import ValidationError
from django.db.models import Q, F, Count
from andr_omeda.andr_moderation.models import ModeratedObject
from andr_omeda.andr_bot.models.bot import Bot
from django.utils.translation import ugettext_lazy as _


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
        query.add(Q(chats__moderated_objects__status=ModeratedObject.STATUS_PENDING), Q.AND)

        if max_id:
            query.add(Q(id__lt=max_id), Q.AND)

        return Bot.objects.filter(query).distinct

    def update_moderated_object_with_id(self, moderated_object_id, description=None,
                                        category_id=None):
        moderated_object = ModeratedObject.objects.get(pk=moderated_object_id)

        return self.update_moderated_object(moderated_object=moderated_object, description=description,
                                            category_id=category_id)

    def update_moderated_object(self, moderated_object, description=None,
                                category_id=None):
        #check_can_update_moderated_object(user=self, moderated_object=moderated_object)
        moderated_object.update_with_actor_with_id(actor_id=self.pk, description=description,
                                                   category_id=category_id)
        return moderated_object

    def reject_moderated_object_with_id(self, moderated_object_id):
        moderated_object = ModeratedObject.objects.get(pk=moderated_object_id)
        return self.reject_moderated_object(moderated_object=moderated_object)

    def reject_moderated_object(self, moderated_object):
        moderated_object.reject_with_actor_with_id(actor_id=self.pk)

    def get_logs_for_moderated_object_with_id(self, moderated_object_id, max_id=None):
        moderated_object = ModeratedObject.objects.get(pk=moderated_object_id)
        return self.get_logs_for_moderated_object(moderated_object=moderated_object, max_id=max_id)

    def get_logs_for_moderated_object(self, moderated_object, max_id=None):
        query = Q()

        if max_id:
            query.add(Q(id__lt=max_id), Q.AND)

        return moderated_object.logs.filter(query)
