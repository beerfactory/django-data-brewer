from rest_framework import viewsets
from data_brewer.models import DataSource, DataStream, Sample
from data_brewer.serializers import DataSourceSerializer


class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer


class DataStreamViewSet(viewsets.ModelViewSet):
    queryset = DataStream.objects.all()
    serializer_class = DataSourceSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = DataSourceSerializer