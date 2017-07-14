# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('tpic', models.ImageField(upload_to=b'goods')),
                ('tprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(default=b'500 g', max_length=20)),
                ('gclick', models.IntegerField(default=0)),
                ('gjianjie', models.CharField(max_length=200)),
                ('gkuncun', models.IntegerField(default=100)),
                ('gcontent', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'typeinfo',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtpye',
            field=models.ForeignKey(to='goods.TypeInfo'),
        ),
    ]
