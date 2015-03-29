from django.utils.translation import ugettext as _
from django.db import models
import jsonfield


class DataSource(models.Model):
    name = models.CharField(_('Data source name'),  max_length=40)
    description = models.CharField(_('Data source description'), max_length=1000, null=True, blank=True)
    metadata = jsonfield.JSONField(_('Data source meta-data'))


class DataStream(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, null=True, blank=True)
    metadata = jsonfield.JSONField()
    data_source = models.ForeignKey(DataSource)


class DataSample(models.Model):
    metadata = jsonfield.JSONField()
    sample_date = models.DateTimeField(null=False)
    record_date = models.DateTimeField(null=False, auto_now_add=True, editable=False)
    value = models.CharField(max_length=100)
    data_stream = models.ForeignKey(DataStream)