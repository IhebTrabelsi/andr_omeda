from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


# TODO switch to custom serializer/model field when possible


class Andrid(models.Model):
    """presents a way for sequencing gathered updates"""
    update = models.OneToOneField(
        "Update",
        on_delete=models.DO_NOTHING,
        related_name="update_id"
    )
    week_order = models.IntegerField(_("week_order"))
    _id = models.TextField(_("_id"), default="undef")
    created = models.DateTimeField(_("created"), editable=False, db_index=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.created:
            self.created = timezone.now()

    # NOTE update_id will be rechosen randomly after one week without
    # new updates

    @classmethod
    def create_andrid(cls, _id):
        last_andrid = cls.objects.order_by('-pk')[0]
        if last_andrid:
            if int(last_andrid._id) == int(_id) - 1:
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
            andrid = Andrid(
                week_order=0,
                _id=_id
            )
            andrid.save()
            return andrid
