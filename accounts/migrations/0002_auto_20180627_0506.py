# Generated by Django 2.0.6 on 2018-06-27 05:06

import accounts.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='snu.ac.kr 계정 이메일을 입력해주세요', max_length=254, unique=True, validators=[accounts.validator.snumail_validator], verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_year',
            field=models.PositiveSmallIntegerField(validators=[accounts.validator.enroll_year_validator], verbose_name='가입 년도'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(help_text='01x-xxxx-xxxx 형식으로 입력해주세요', max_length=14, validators=[accounts.validator.phone_validator], verbose_name='전화번호'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_no',
            field=models.CharField(help_text='20xx-xxxxx 형식으로 입력해주세요', max_length=12, unique=True, validators=[accounts.validator.student_no_validator], verbose_name='학번'),
        ),
    ]
