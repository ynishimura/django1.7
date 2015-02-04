# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('misl_viewer', '0003_auto_20150114_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
    ]
