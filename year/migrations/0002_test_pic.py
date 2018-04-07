# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('year', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='pic',
            field=models.ImageField(default='', upload_to='img'),
        ),
    ]
