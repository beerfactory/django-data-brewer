from django.utils.translation import ugettext as _
from django.db import models
import jsonfield


class DataSource(models.Model):
    name = models.CharField(_('Name'),  max_length=40)
    description = models.CharField(_('Description'), max_length=1000, null=True, blank=True)
    metadata = jsonfield.JSONField(_('Metadata'))


class DataStream(models.Model):
    name = models.CharField(_('Name'),  max_length=40)
    description = models.CharField(_('Description'), max_length=1000, null=True, blank=True)
    metadata = jsonfield.JSONField(_('Metadata'))
    data_source = models.ForeignKey(DataSource)


SAMPLE_STATUS = (
    ('NEW', _('New sample')),
    ('EXPIRED', _('Expired sample')),
)


class Sample(models.Model):
    sampling_date = models.DateTimeField(_('Sampling date'), null=False)
    record_date = models.DateTimeField(_('Record date'), null=False, auto_now_add=True, editable=False)
    mean_value = models.DecimalField(_('Mean value'), max_digits=21, decimal_places=9)
    min_value = models.DecimalField(_('Min value'), max_digits=21, decimal_places=9)
    max_value = models.DecimalField(_('Max value'), max_digits=21, decimal_places=9)
    sample_size = models.IntegerField(_('Sample size'), default=1)
    metadata = jsonfield.JSONField(_('Metadata'))
    status = models.CharField(max_length=10, choices=SAMPLE_STATUS, default='NEW')
    data_stream = models.ForeignKey(DataStream)

    @property
    def value(self):
        return self.mean_value

    @value.setter
    def value(self, v):
        self.mean_value = v
        self.min_value = v
        self.max_value = v
        self.sample_size = 1