# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=40)),
                ('description', models.CharField(null=True, blank=True, verbose_name='Description', max_length=1000)),
                ('metadata', jsonfield.fields.JSONField(verbose_name='Metadata', default=dict)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataStream',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=40)),
                ('description', models.CharField(null=True, blank=True, verbose_name='Description', max_length=1000)),
                ('metadata', jsonfield.fields.JSONField(verbose_name='Metadata', default=dict)),
                ('data_source', models.ForeignKey(to='data_brewer.DataSource')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('sampling_date', models.DateTimeField(verbose_name='Sampling date')),
                ('record_date', models.DateTimeField(verbose_name='Record date', auto_now_add=True)),
                ('mean_value', models.DecimalField(verbose_name='Mean value', max_digits=21, decimal_places=9)),
                ('min_value', models.DecimalField(verbose_name='Min value', max_digits=21, decimal_places=9)),
                ('max_value', models.DecimalField(verbose_name='Max value', max_digits=21, decimal_places=9)),
                ('sample_size', models.IntegerField(verbose_name='Sample size', default=1)),
                ('metadata', jsonfield.fields.JSONField(verbose_name='Metadata', default=dict)),
                ('status', models.CharField(default='NEW', choices=[('NEW', 'New sample'), ('EXPIRED', 'Expired sample')], max_length=10)),
                ('data_stream', models.ForeignKey(to='data_brewer.DataStream')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
