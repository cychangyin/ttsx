# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=30)),
                ('upasswd', models.CharField(max_length=255)),
                ('uemail', models.CharField(max_length=50)),
                ('ushou', models.CharField(default=b'', max_length=30)),
                ('uaddrees', models.CharField(default=b'', max_length=100)),
                ('upostalcode', models.IntegerField(default=0)),
                ('uphone', models.CharField(default=b'', max_length=20)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
