# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misl_viewer', '0004_image_upload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='set_threshold',
            field=models.CharField(default=b'DEFAULT_THRESHOLD', max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
