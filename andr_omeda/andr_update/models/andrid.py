from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


# TODO switch to custom serializer/model field when possible


class Andrid(models.Model):
    """presents a way for sequencing gathered updates"""
    week_order = models.IntegerField(_("week_order"), default=0, blank=False)
    _id = models.BigIntegerField(_("_id"), default=-1, blank=False)
    created = models.DateTimeField(_("created"), editable=False, db_index=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.created:
            self.created = timezone.now()
        super().save(*args, **kwargs)

    def get_id(self):
        """only used with populated Andrid object"""
        return self._id

    # NOTE update_id will be rechosen randomly after one week without
    # new updates

    @classmethod
    def create_andrid(cls, *args, **kwargs):
        _id = kwargs.get('_id', None)
        if not _id:
            _id = args[0]
        if not list(cls.objects.all()):
            andrid = Andrid(
                week_order=1,
                _id=_id
            )
            andrid.save()
            return andrid
        last_andrid = cls.objects.order_by('-pk')[0]
        if last_andrid:
            if int(last_andrid.get_id()) == int(_id) - 1:
                andrid = Andrid(
                    week_order=last_andrid.week_order,
                    _id=_id
                )
                andrid.save()
                return andrid
            else:
                week_order_incr = last_andrid.week_order + 1
                andrid = Andrid(
                    week_order=week_order_incr,
                    _id=_id
                )
                andrid.save()
                return andrid
        else:
            raise Exception('can\'t access andrid in db')
