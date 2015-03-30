from django.contrib import admin
from data_brewer.models import DataSource, DataStream, Sample

# Register your models here.
admin.site.register(DataSource)
admin.site.register(DataStream)
admin.site.register(Sample)