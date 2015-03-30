from rest_framework import serializers
from data_brewer.models import DataSource, DataStream, Sample


class DataSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataSource


class DataStreamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataStream


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sample