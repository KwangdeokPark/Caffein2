# Generated by Django 2.0.6 on 2018-07-22 07:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_auto_20180721_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meeting_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 22, 7, 56, 8, 240997, tzinfo=utc), verbose_name='날짜 및 시간'),
        ),
    ]
