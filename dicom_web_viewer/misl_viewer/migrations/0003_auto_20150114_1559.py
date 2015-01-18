# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misl_viewer', '0002_auto_20150109_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='upload_date',
        ),
        migrations.AddField(
            model_name='image',
            name='set_proc',
            field=models.CharField(default=b'DEFAULT_PROC', max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='set_tag',
            field=models.CharField(default=b'DEFAULT_TAG', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
