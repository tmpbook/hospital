# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20150511_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('com_ID', models.CharField(max_length=20)),
                ('user_ID', models.CharField(max_length=20)),
                ('pro_ID', models.CharField(max_length=20)),
                ('com_content', models.IntegerField()),
                ('com_time', models.DateField()),
                ('com_status', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_ID', models.CharField(max_length=20)),
                ('hos_ID', models.CharField(max_length=20)),
                ('doc_name', models.CharField(max_length=50)),
                ('doc_professional', models.CharField(max_length=100)),
                ('doc_profile', models.CharField(max_length=500)),
                ('doc_grade', models.CharField(max_length=20)),
                ('doc_depart', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hos_ID', models.CharField(max_length=20)),
                ('hos_name', models.CharField(max_length=50)),
                ('hos_palce', models.CharField(max_length=100)),
                ('hos_profile', models.CharField(max_length=1000)),
                ('hos_rating', models.CharField(max_length=20)),
                ('hos_grade', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('hos_prope', models.CharField(default=b'public', max_length=10, choices=[(b'public', b'\xe5\x85\xac\xe7\xab\x8b\xe5\x8c\xbb\xe9\x99\xa2'), (b'private', b'\xe7\xa7\x81\xe7\xab\x8b\xe5\x8c\xbb\xe9\x99\xa2')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_ID', models.CharField(max_length=20)),
                ('user_ID', models.CharField(max_length=20)),
                ('news_title', models.IntegerField()),
                ('news_image', models.CharField(max_length=50)),
                ('news_time', models.DateField()),
                ('news_name', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_ID', models.CharField(max_length=20)),
                ('user_ID', models.CharField(max_length=50)),
                ('pro_ID', models.CharField(max_length=20)),
                ('order_name', models.CharField(max_length=200)),
                ('order_time', models.DateField()),
                ('order_batch', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_ID', models.CharField(max_length=20)),
                ('pay_ID', models.CharField(max_length=20)),
                ('pay_money', models.IntegerField()),
                ('pay_time', models.DateField()),
                ('pay_mark', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro_ID', models.CharField(max_length=20)),
                ('doc_ID', models.CharField(max_length=20)),
                ('hos_ID', models.CharField(max_length=20)),
                ('pro_detail', models.CharField(max_length=500)),
                ('pro_depart', models.CharField(max_length=200)),
                ('pro_standard', models.CharField(max_length=500)),
                ('pro_time', models.DateField()),
                ('pro_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
