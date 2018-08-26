# Generated by Django 2.0.6 on 2018-08-26 07:07

import cafe.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='카페이름')),
                ('address', models.CharField(max_length=200, verbose_name='주소')),
                ('description', models.TextField(blank=True, verbose_name='설명')),
                ('phone', models.CharField(blank=True, max_length=14, verbose_name='전화번호')),
                ('machine', models.CharField(blank=True, max_length=100, verbose_name='에스프레소 머신')),
                ('grinder', models.CharField(blank=True, max_length=100, verbose_name='그라인더')),
                ('price', models.CharField(blank=True, choices=[('CHEAPEST', '~ 2천원'), ('CHEAP', '2천원 ~ 4천원'), ('MIDDLE', '4천원 ~ 6천원'), ('EXPENSIVE', '6천원 ~ 8천원'), ('MOST EXPENSIVE', '8천원 ~ ')], max_length=15, verbose_name='가격대')),
                ('from_time', models.TimeField(blank=True, null=True, verbose_name='개점시간')),
                ('to_time', models.TimeField(blank=True, null=True, verbose_name='폐점시간')),
                ('closed_day', models.CharField(blank=True, choices=[('SUN', '일요일'), ('MON', '월요일'), ('TUE', '화요일'), ('WED', '수요일'), ('THU', '목요일'), ('FRI', '금요일'), ('SAT', '토요일')], max_length=3, verbose_name='휴무일')),
                ('closed_frq', models.CharField(blank=True, choices=[('EVERY', '매주'), ('FIRST', '첫번째'), ('SECOND', '두번째'), ('THIRD', '세번째'), ('FOURTH', '네번째'), ('LAST', '마지막')], max_length=6, verbose_name='휴무 빈도')),
                ('closed_holiday', models.BooleanField(default=False, verbose_name='공휴일 휴무 여부')),
                ('image', models.ImageField(blank=True, upload_to=cafe.models.get_cafe_photo_path, verbose_name='이미지')),
                ('link', models.CharField(blank=True, max_length=260, validators=[django.core.validators.URLValidator()], verbose_name='홈페이지')),
                ('road_address', models.CharField(blank=True, max_length=100, verbose_name='도로명주소')),
                ('mapx', models.IntegerField(blank=True, null=True, verbose_name='x좌표')),
                ('mapy', models.IntegerField(blank=True, null=True, verbose_name='y좌표')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '카페',
                'verbose_name_plural': '카페',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='cafe',
            unique_together={('name', 'address')},
        ),
    ]
