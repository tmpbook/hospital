# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_comments_doctor_hospital_news_order_payment_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pro_user',
            field=models.CharField(default=1998, max_length=50),
            preserve_default=False,
        ),
    ]
