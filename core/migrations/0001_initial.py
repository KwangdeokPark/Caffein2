# Generated by Django 2.0.6 on 2018-06-30 06:28

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
                ('image', models.ImageField(upload_to=core.models.get_feed_photo_path)),
            ],
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
            name='OperationScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_start', models.DateField(verbose_name='학기 시작일')),
                ('semester_end', models.DateField(blank=True, null=True, verbose_name='학기 종료일')),
                ('new_register_start', models.DateTimeField(verbose_name='신입 가입 시작일')),
                ('new_register_end', models.DateTimeField(verbose_name='신입 가입 종료일')),
                ('old_register_start', models.DateTimeField(verbose_name='기존 가입 시작일')),
                ('old_register_end', models.DateTimeField(verbose_name='기존 가입 종료일')),
                ('bank_account', models.CharField(max_length=30, verbose_name='입금 계좌')),
                ('bank', models.CharField(choices=[('kb', 'KB국민은행'), ('nh', 'NH농협'), ('sh', '신한은행'), ('wr', '우리은행'), ('hn', '하나(구 외환)'), ('kk', '케이뱅크'), ('ka', '카카오뱅크'), ('kd', 'KDB산업은행'), ('ib', 'IBK기업은행'), ('sh', '수협은행'), ('sm', '새마을금고')], max_length=2, verbose_name='입금 은행')),
                ('new_pay', models.PositiveIntegerField(verbose_name='신입회원 가입비')),
                ('old_pay', models.PositiveIntegerField(verbose_name='기존회원 가입비')),
                ('boss', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.ActiveUser')),
            ],
        ),
        migrations.CreateModel(
            name='PostedPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=core.models.get_posted_photo_path)),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=20, verbose_name='제목')),
                ('content', models.TextField(max_length=1000, verbose_name='내용')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='postedphotos',
            name='posting',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Posting'),
        ),
        migrations.AddField(
            model_name='feedphotos',
            name='instagram',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Instagram'),
        ),
    ]