from django.utils.translation import ugettext_lazy as _
from django.db import models


class FLOW(models.IntegerChoices):
    pass


SHOULD_ACCEPT_TERMS = (1,)
FETCH_LAST_FILLLED_STER = (2,)
CHOOSE_LANGUAGE = (3,)
ADD_ROW = (4,)
DELETE_ROW = (5,)
SUBMIT_TABLE = (6,)
ABORT = (7,)
GREET = (8,)

NEW_MEMBER_FLOW = [
    (SHOULD_ACCEPT_TERMS[0], _('terms'))
]


IDLE_FLOW = [
    (GREET[0], _('show welcome message.')),
    (FETCH_LAST_FILLLED_STER[0], _('get my last filled steuererklaerung table.')),
    (CHOOSE_LANGUAGE[0], _('choose between en or de.'))
]

STER_TABLE_FILL_FLOW = [
    (ADD_ROW[0], _('add new row')),
    (DELETE_ROW[0], _('delete row')),
    (SUBMIT_TABLE[0], _('submit the table')),
    (ABORT[0], _('exit'))
]

FLOW = NEW_MEMBER_FLOW + IDLE_FLOW + STER_TABLE_FILL_FLOW
