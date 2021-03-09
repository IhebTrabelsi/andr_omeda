from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# TODO switch to custom serializer/model field when possible


class Andrid(models.Model):
    """presents a way for sequencing gathered updates"""

    week_order = models.IntegerField(_("week_order"))
    update_id = models.CharField(_("update_id"), default="undef")
    created = models.DateTimeField(_("created"), default=timezone.now())

    # NOTE update_id will be rechosen randomly after one week without
    # new updates
    @classmethod
    def create_andrid(cls, update_id):
        last_andrid = cls.objects.order_by('-pk')[0]
        if last_andrid:
            if int(last_andrid.update_id) == int(update_id) - 1:
                andrid = Andrid(
                    week_order=last_andrid.week_order,
                    update_id=update_id
                )
                andrid.save()
                return andrid
            else:
                week_order_incr = last_andrid.week_order + 1
                andrid = Andrid(
                    week_order=week_order_incr,
                    update_id=update_id
                )
                andrid.save()
                return andrid
        else:
            andrid = Andrid(
                week_order=0,
                update_id=update_id
            )
            andrid.save()
            return andrid
