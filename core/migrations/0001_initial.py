# Generated by Django 2.0.6 on 2018-08-26 07:07

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=core.models.get_feed_photo_path)),
            ],
            options={
                'verbose_name': '피드 사진',
                'verbose_name_plural': '피드 사진',
            },
        ),
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=1000, verbose_name='내용')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(max_length=1000, verbose_name='내용')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='제목')),
                ('meeting_date', models.DateTimeField(verbose_name='날짜 및 시간')),
                ('max_participants', models.PositiveSmallIntegerField(default=0, help_text='인원제한을 없애려면 0으로 설정하세요.', verbose_name='참석 인원')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
                ('participants', models.ManyToManyField(to='accounts.ActiveUser', verbose_name='참석자')),
            ],
            options={
                'verbose_name': '모임',
                'verbose_name_plural': '모임',
                'get_latest_by': ['-meeting_date'],
            },
        ),
        migrations.CreateModel(
            name='MeetingPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=core.models.get_meeting_photo_path)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='core.Meeting', verbose_name='모임')),
            ],
            options={
                'verbose_name': '모임 사진',
                'verbose_name_plural': '모임 사진',
            },
        ),
        migrations.CreateModel(
            name='OperationScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_start', models.DateField(help_text='1학기는 3월 2일, 2학기는 9월 1일', verbose_name='학기 시작일')),
                ('semester_end', models.DateField(blank=True, default=None, null=True, verbose_name='학기 종료일')),
                ('new_register_start', models.DateTimeField(verbose_name='신입 가입 시작일')),
                ('new_register_end', models.DateTimeField(blank=True, null=True, verbose_name='신입 가입 종료일')),
                ('old_register_start', models.DateTimeField(verbose_name='기존 가입 시작일')),
                ('old_register_end', models.DateTimeField(blank=True, null=True, verbose_name='기존 가입 종료일')),
                ('coffee_point', models.FloatField(default=2.0, help_text='실수형 점수입니다. 예: 2.0', verbose_name='커모 1회당 점수')),
                ('eat_point', models.FloatField(default=1.0, help_text='실수형 점수입니다. 예: 2.0', verbose_name='밥모 1회당 점수')),
                ('bank_account', models.CharField(max_length=30, verbose_name='입금 계좌')),
                ('bank', models.CharField(choices=[('kb', 'KB국민은행'), ('nh', 'NH농협'), ('sh', '신한은행'), ('wr', '우리은행'), ('hn', '하나(구 외환)'), ('kk', '케이뱅크'), ('ka', '카카오뱅크'), ('kd', 'KDB산업은행'), ('ib', 'IBK기업은행'), ('sh', '수협은행'), ('sm', '새마을금고')], max_length=2, verbose_name='입금 은행')),
                ('new_pay', models.PositiveIntegerField(verbose_name='신입회원 가입비')),
                ('old_pay', models.PositiveIntegerField(verbose_name='기존회원 가입비')),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.ActiveUser')),
            ],
            options={
                'verbose_name': '운영 정보',
                'verbose_name_plural': '운영 정보',
            },
        ),
        migrations.AddField(
            model_name='feedphotos',
            name='instagram',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='core.Instagram', verbose_name='인스타'),
        ),
    ]
