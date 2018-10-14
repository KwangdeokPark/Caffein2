# Generated by Django 2.0.6 on 2018-10-09 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20181009_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationscheme',
            name='extra_author_point',
            field=models.FloatField(default=2.0, help_text='커모를 개최하는 사람에게 추가로 부여하는 점수입니다.커모 개최자에게 커모점수 + 개최자 추가 점수', verbose_name='커모 개최자 추가 점수'),
        ),
    ]