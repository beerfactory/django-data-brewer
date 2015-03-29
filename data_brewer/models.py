from django.utils.translation import ugettext as _
from django.db import models
import jsonfield


class DataSource(models.Model):
    name = models.CharField(_('Data source name'),  max_length=40)
    description = models.CharField(_('Data source description'), max_length=1000, null=True, blank=True)
    metadata = jsonfield.JSONField(_('Data source meta-data'))


class DataStream(models.Model):
    name = models.CharField(_('Stream name'),  max_length=40)
    description = models.CharField(_('Stream description'), max_length=1000, null=True, blank=True)
    metadata = jsonfield.JSONField(_('Stream meta-data'))
    data_source = models.ForeignKey(DataSource)


SAMPLE_STATUS = (
    ('NEW', _('New sample')),
    ('OBSOLETE', _('Obsolete sample')),
)


class DataSample(models.Model):
    metadata = jsonfield.JSONField(_('Sample metadata'))
    sample_date = models.DateTimeField(_('Sample sampling date'), null=False)
    record_date = models.DateTimeField(_('Sample record date'), null=False, auto_now_add=True, editable=False)
    value = models.CharField(_('Sample value'), max_length=100)
    data_stream = models.ForeignKey(DataStream)
    status = models.CharField(max_length=10, choices=SAMPLE_STATUS)