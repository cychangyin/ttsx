# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttusers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='upasswd',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upostalcode',
            field=models.CharField(default=b'', max_length=8),
        ),
    ]
