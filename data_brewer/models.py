from django.db import models
import jsonfield


class DataSource(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, null=True)
    metadata = jsonfield.JSONField()

class DataStream(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000, null=True)
    metadata = jsonfield.JSONField()
    data_source = models.ForeignKey(DataSource)


class DataPoint(models.Model):
    metadata = jsonfield.JSONField()
    timestamp = models.DateTimeField(null=False)
    value = models.CharField(max_length=100)
    data_stream = models.ForeignKey(DataStream)