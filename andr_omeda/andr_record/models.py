from django.db import models
from django.utils.translation import ugettext_lazy as _
from andr_omeda.andr_update import choices
from django.contrib.postgres.fields import ArrayField
from andr_omeda.andr_base.utils.related import AutoOneToOneField

"""
-->new user starts conversation with bot 
----->Update
----->bot tableau created
-------->if new_user
            -create user record & bind to an entry in tableau
-------->else
            -get user record from tableau for entry appartient à ce user 
            - get # action to be done (userrecord.action):
                ex:
                    [one step events]
                    - send record to erpnext ?

                    ?????????????????????????????????????????????????????????
                    [multiple steps events]    * maybe each event execution time should only be
                    determined by task -> when finished update record

                    - still filling steuererklaerung tableau ?
                    - steuererklaerung tableau finished ?
                    ...
                    ?????????????????????????????????????????????????????????
                    [errors]
                    - error type ?
                    
<----------- return 200

            ////////////////////////////////////////////////////////////

                - entry version = ex:50
                - userrecord.last_



======> COMPLEX / TIME CONSUMING / MAY BE LATER IMPLEMENTED FOR OPTIMIZATION

"""

"""
SYNC

PER UPDATE , ON EACH TELEGRAM DATA TYPE CREATION EX: MESSAGE CREATION


* minimal state records in database for previous several request/response cycles

  ex: for events that persist for several requests 
    

"""


"""
choices.py : 

steuererklaerung_fill = 
{

}
------------------------------------------

chat model:

--> "what to expect in next requests that flow execution must act accordinaly"
flow_queue = 
[
    {choice1:a, choice2:b, choice3:c},
    ...,
    {choice2:a}
]
"""


def _table_layout():
    return {
        'columns-max-number': 2,
        'rows-max-number': 100,
        'columns': [
            {
                'col-prefix': 'fields',
                'read-only': False
            },
            {
                'col-prefix': 'values',
                'read-only': True
            }
        ]
    }


def _table_data():
    return {
        'rows': [
            {
                'values': [{'value': 'ping'} for v in range(_table_layout()['columns-max-number'])]
            }
        ]
    }


class Record(models.Model):
    andruser = models.ForeignKey(
        "andr_update.Andruser",
        on_delete=models.CASCADE,
        null=True,
        related_name="records"
    )

    is_draft = models.BooleanField(
        _('is_draft'),
        default=True
    )

    class Meta:
        abstract = True


class STERRecord(Record):
    table_layout = models.JSONField(default=_table_layout)
    table_data = models.JSONField(default=_table_data)

    is_submitted = models.BooleanField(
        _('is_submitted'),
        default=False
    )

    def submit(self):
        self.is_submitted = True
        self.is_draft = False

    def add_row_value(self, key, value):
        pass

    def _get_read_value_for_col_and_row(self, col, row):
        return {'value': 'bingo'}

    def add_row(self, **entries):
        """
        entries: (column_prefix : value)
        """
        row = []
        for col in self.table_layout['columns']:
            if not entries.get(col['col-prefix'], None):
                continue
            if not col['read-only']:
                row.append(
                    {'value': entries[col['col-prefix']]}
                )
            else:
                row.append(self._get_read_value_for_col_and_row(col, row))

        self.table_data['rows'].append(
            {
                'values': row
            }
        )

        self.save()

# ===============================================================================
#
#                                 FLOW-QUEUE
#
# ===============================================================================


"""
chat_id not unique for each bot per user 
to distinguish between seperate chats in different bots :
    chat_id to distinguish the user + token to distinguish which bot
"""


class FlowNode(models.Model):
    event = models.IntegerField(choices=choices.FLOW)


def _def_queue():
    return [choices.WAITING_FOR_APPROVAL[0]]


def _def_update_queue():
    return []


class FlowQueue(models.Model):
    chat = models.OneToOneField(
        "andr_update.Chat",
        on_delete=models.CASCADE,
        related_name="flow_queue",
        null=True
    )

    queue = ArrayField(
        models.IntegerField(),
        default=_def_queue
    )

    last_update_uuid = ArrayField(
        models.UUIDField(),
        default=_def_update_queue
    )

    def get_last_queue_state(self):
        return self.queue[-1]

    def no_prev_uuid(self):
        return len(self.last_update_uuid) <= 1

    def get_prev_uuid(self):
        return self.last_update_uuid[-2]

    def append_state(self, state):
        self.queue.append(state)
        self.save()
