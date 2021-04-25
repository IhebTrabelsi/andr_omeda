from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from andr_omeda.andr_update.models import Update


class InlineQuery(models.Model):
    inline_query_from = models.ForeignKey(
        "Andruser",
        on_delete=models.CASCADE,
        related_name="inline_query",
        blank=True,
        null=True
    )
    inline_query_id = models.TextField(_("inline_query_id"), blank=False)
    query = models.TextField(_("query"), blank=True)
    offset = models.TextField(_("offset"), blank=True)

    @classmethod
    def inlinequery_id_sanitize(cls, data, *args, **kwargs):
        if data.get('inline_query', None):
            data['inline_query']['inline_query_id'] = data['inline_query']['id']
            del data['inline_query']['id']
        return data

    @classmethod
    def inlinequery_validation(cls, data, *args, **kwargs):
        _data = cls.inlinequery_id_sanitize(data)
        if _data.get('inline_query', None):
            if not _data.get('inline_query').get('location', None):
                _data['inline_query']['location'] = {}
            _query = _data.get('inline_query').get('query', None)
            if not _query and not len(_query) == 0:
                _data['inline_query']['query'] = ''
            _offset = _data.get('inline_query').get('offset', None)
            if not _offset and not len(_offset) == 0:
                _data['inline_query']['offset'] = ''
        return _data
