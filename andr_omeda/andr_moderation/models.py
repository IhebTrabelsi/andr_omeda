from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from django.utils import timezone
from mixer.backend.django import mixer


class ModerationCategory(models.Model):
    name = models.CharField(_('name'), max_length=32, blank=False, null=False)
    title = models.CharField(_('title'), max_length=64, blank=False, null=False)
    description = models.CharField(_('description'), max_length=255, blank=False, null=False)
    created = models.DateTimeField(editable=False, db_index=True)
    order = models.PositiveSmallIntegerField(editable=False)

    SEVERITY_CRITICAL = 'C'
    SEVERITY_HIGH = 'H'
    SEVERITY_MEDIUM = 'M'
    SEVERITY_LOW = 'L'
    SEVERITIES = (
        (SEVERITY_CRITICAL, 'Critical'),
        (SEVERITY_HIGH, 'High'),
        (SEVERITY_MEDIUM, 'Medium'),
        (SEVERITY_LOW, 'Low'),
    )

    severity = models.CharField(max_length=5, choices=SEVERITIES)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id and not self.created:
            self.created = timezone.now()

        return super(ModerationCategory, self).save(*args, **kwargs)

    @classmethod
    def make_moderation_category(cls, severity=SEVERITY_MEDIUM):
        return mixer.blend(cls, severity=severity)


class ModeratedObject(models.Model):
    description = models.CharField(_('description'), max_length=4096,
                                   blank=False, null=True)
    verified = models.BooleanField(_('verified'), default=False,
                                   blank=False, null=False)

    STATUS_PENDING = 'P'
    STATUS_APPROVED = 'A'
    STATUS_REJECTED = 'R'

    STATUSES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    )

    status = models.CharField(max_length=5, choices=STATUSES, default=STATUS_PENDING)

    category = models.ForeignKey(ModerationCategory, on_delete=models.CASCADE, related_name='moderated_objects')

    bot = models.ForeignKey("andr_bot.Bot", on_delete=models.CASCADE, null=True)

    OBJECT_TYPE_CHAT = 'C'

    OBJECT_TYPES = (
        (OBJECT_TYPE_CHAT, 'Chat'),
    )

    object_type = models.CharField(max_length=5, choices=OBJECT_TYPES)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    class Meta:
        constraints = [
            models.UniqueConstraint(name='reporter_moderated_object_constraint',
                                    fields=['object_type', 'object_id'])
        ]

    @classmethod
    def create_moderated_object(cls, object_type, bot, content_object, category_id):
        return cls.objects.create(object_type=object_type, bot=bot, content_object=content_object,
                                  category_id=category_id)

    @classmethod
    def _get_or_create_moderated_object(cls, object_type, bot, content_object, category_id):
        # category_id makes sense only in object creation, for retreiving, we get
        # what's been already created
        try:
            moderated_object = cls.objects.get(object_type=object_type, bot=bot, object_id=content_object.pk)
        except cls.DoesNotExist:
            moderated_object = cls.create_moderated_object(object_type=object_type,
                                                           bot=bot,
                                                           content_object=content_object,
                                                           category_id=category_id)

        return moderated_object

    @classmethod
    def get_or_create_moderated_object_for_chat(cls, bot, chat, category_id):
        return cls._get_or_create_moderated_object(object_type=cls.OBJECT_TYPE_CHAT,
                                                   bot=bot,
                                                   content_object=chat,
                                                   category_id=category_id)

    def is_verified(self):
        return self.verified

    def is_approved(self):
        return self.status == ModeratedObject.STATUS_APPROVED

    def is_pending(self):
        return self.status == ModeratedObject.STATUS_PENDING

    @classmethod
    def check_moderation_approved(cls, chat_id, token):
        mod_ob = cls.objects.get(chats__chat_id=chat_id, bot__token=token)
        return mod_ob.is_approved()

    def update_with_actor_with_id(self, actor_id, description, category_id):
        if description is not None:
            current_description = self.description
            self.description = description
            ModeratedObjectDescriptionChangedLog.create_moderated_object_description_changed_log(
                changed_from=current_description, changed_to=description, moderated_object_id=self.pk,
                actor_id=actor_id)

        if category_id is not None:
            current_category_id = self.category_id
            self.category_id = category_id
            ModeratedObjectCategoryChangedLog.create_moderated_object_category_changed_log(
                changed_from_id=current_category_id, changed_to_id=category_id, moderated_object_id=self.pk,
                actor_id=actor_id)

        self.save()

    def verify_with_actor_with_id(self, actor_id):
        current_verified = self.verified
        self.verified = True
        ModeratedObjectVerifiedChangedLog.create_moderated_object_verified_changed_log(
            changed_from=current_verified, changed_to=self.verified, moderated_object_id=self.pk, actor_id=actor_id)

        self.save()

    def unverify_with_actor_with_id(self, actor_id):
        current_verified = self.verified
        self.verified = False
        ModeratedObjectVerifiedChangedLog.create_moderated_object_verified_changed_log(
            changed_from=current_verified, changed_to=self.verified, moderated_object_id=self.pk, actor_id=actor_id)

        self.save()

    def approve_with_actor_with_id(self, actor_id):
        current_status = self.status
        self.status = ModeratedObject.STATUS_APPROVED
        ModeratedObjectStatusChangedLog.create_moderated_object_status_changed_log(
            changed_from=current_status, changed_to=self.status, moderated_object_id=self.pk, actor_id=actor_id)

        self.save()

    def reject_with_actor_with_id(self, actor_id):
        current_status = self.status
        self.status = ModeratedObject.STATUS_REJECTED
        ModeratedObjectStatusChangedLog.create_moderated_object_status_changed_log(
            changed_from=current_status, changed_to=self.status, moderated_object_id=self.pk, actor_id=actor_id)
        self.save()


class ModeratedObjectLog(models.Model):
    actor = models.ForeignKey("andr_bot.BotERPOwner", on_delete=models.CASCADE, related_name='+', null=True)

    LOG_TYPE_DESCRIPTION_CHANGED = 'DC'
    LOG_TYPE_STATUS_CHANGED = 'AC'
    LOG_TYPE_VERIFIED_CHANGED = 'VC'
    LOG_TYPE_CATEGORY_CHANGED = 'CC'

    LOG_TYPES = (
        (LOG_TYPE_DESCRIPTION_CHANGED, 'Description Changed'),
        (LOG_TYPE_STATUS_CHANGED, 'Status Changed'),
        (LOG_TYPE_VERIFIED_CHANGED, 'Verified Changed'),
        (LOG_TYPE_CATEGORY_CHANGED, 'Category Changed'),
    )

    log_type = models.CharField(max_length=5, choices=LOG_TYPES)

    # Generic relation types
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    moderated_object = models.ForeignKey(ModeratedObject, on_delete=models.CASCADE, related_name='logs')
    created = models.DateTimeField(editable=False, db_index=True)

    @classmethod
    def create_moderated_object_log(cls, moderated_object_id, log_type, content_object, actor_id):
        return cls.objects.create(log_type=log_type, content_object=content_object,
                                  moderated_object_id=moderated_object_id,
                                  actor_id=actor_id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id and not self.created:
            self.created = timezone.now()

        return super(ModeratedObjectLog, self).save(*args, **kwargs)


class ModeratedObjectDescriptionChangedLog(models.Model):
    log = GenericRelation(ModeratedObjectLog)
    changed_from = models.CharField(_('changed from'), max_length=4096,
                                    blank=False, null=True)
    changed_to = models.CharField(_('changed to'), max_length=4096,
                                  blank=False, null=True)

    @classmethod
    def create_moderated_object_description_changed_log(cls, moderated_object_id, changed_from, changed_to, actor_id):
        moderated_object_description_changed_log = cls.objects.create(changed_from=changed_from,
                                                                      changed_to=changed_to)
        ModeratedObjectLog.create_moderated_object_log(log_type=ModeratedObjectLog.LOG_TYPE_DESCRIPTION_CHANGED,
                                                       content_object=moderated_object_description_changed_log,
                                                       moderated_object_id=moderated_object_id,
                                                       actor_id=actor_id)


class ModeratedObjectCategoryChangedLog(models.Model):
    log = GenericRelation(ModeratedObjectLog)
    changed_from = models.ForeignKey(ModerationCategory, on_delete=models.CASCADE, related_name='+')
    changed_to = models.ForeignKey(ModerationCategory, on_delete=models.CASCADE, related_name='+')

    @classmethod
    def create_moderated_object_category_changed_log(cls, moderated_object_id, changed_from_id, changed_to_id,
                                                     actor_id):
        moderated_object_category_changed_log = cls.objects.create(changed_from_id=changed_from_id,
                                                                   changed_to_id=changed_to_id)
        ModeratedObjectLog.create_moderated_object_log(log_type=ModeratedObjectLog.LOG_TYPE_CATEGORY_CHANGED,
                                                       content_object=moderated_object_category_changed_log,
                                                       moderated_object_id=moderated_object_id, actor_id=actor_id)


class ModeratedObjectVerifiedChangedLog(models.Model):
    log = GenericRelation(ModeratedObjectLog)
    changed_from = models.BooleanField(_('changed from'),
                                       blank=False, null=False)
    changed_to = models.BooleanField(_('changed to'),
                                     blank=False, null=False)

    @classmethod
    def create_moderated_object_verified_changed_log(cls, moderated_object_id, changed_from, changed_to, actor_id):
        moderated_object_description_changed_log = cls.objects.create(changed_from=changed_from,
                                                                      changed_to=changed_to)
        ModeratedObjectLog.create_moderated_object_log(log_type=ModeratedObjectLog.LOG_TYPE_VERIFIED_CHANGED,
                                                       content_object=moderated_object_description_changed_log,
                                                       moderated_object_id=moderated_object_id, actor_id=actor_id)


class ModeratedObjectStatusChangedLog(models.Model):
    log = GenericRelation(ModeratedObjectLog)
    changed_from = models.CharField(_('changed from'),
                                    choices=ModeratedObject.STATUSES,
                                    blank=False, null=False, max_length=5)
    changed_to = models.CharField(_('changed to'),
                                  blank=False, null=False, max_length=5)

    @classmethod
    def create_moderated_object_status_changed_log(cls, moderated_object_id, changed_from, changed_to, actor_id):
        moderated_object_description_changed_log = cls.objects.create(changed_from=changed_from,
                                                                      changed_to=changed_to)
        ModeratedObjectLog.create_moderated_object_log(log_type=ModeratedObjectLog.LOG_TYPE_STATUS_CHANGED,
                                                       content_object=moderated_object_description_changed_log,
                                                       moderated_object_id=moderated_object_id, actor_id=actor_id)
