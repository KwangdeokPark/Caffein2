# Generated by Django 2.0.6 on 2018-07-21 12:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0003_auto_20180721_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meeting_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 12, 36, 30, 647118, tzinfo=utc), verbose_name='날짜 및 시간'),
        ),
    ]
