# Generated by Django 2.0.6 on 2018-10-06 21:26

import accounts.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_year', models.PositiveSmallIntegerField(validators=[accounts.validators.year_validator], verbose_name='짝지 연도')),
                ('partner_semester', models.PositiveSmallIntegerField(choices=[(1, '1학기'), (2, '2학기')], verbose_name='짝지 학기')),
                ('score', models.FloatField(default=0.0, verbose_name='짝지 점수')),
                ('down_partner_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partners1', to='accounts.ActiveUser')),
                ('down_partner_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partners2', to='accounts.ActiveUser')),
                ('down_partner_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partners3', to='accounts.ActiveUser')),
                ('up_partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ActiveUser')),
            ],
            options={
                'verbose_name': '짝지',
                'verbose_name_plural': '짝지',
                'get_latest_by': ['-partner_year', 'partner_semester'],
            },
        ),
        migrations.CreateModel(
            name='PartnerMeeting',
            fields=[
                ('instagram_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Instagram')),
                ('num_coffee', models.SmallIntegerField(default=0, verbose_name='마신 커피 수')),
                ('num_eat', models.SmallIntegerField(default=0, verbose_name='먹은 식사 수')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
            ],
            options={
                'verbose_name': '짝지 모임',
                'verbose_name_plural': '짝지 모임',
            },
            bases=('core.instagram',),
        ),
        migrations.AlterUniqueTogether(
            name='partner',
            unique_together={('partner_year', 'partner_semester', 'up_partner')},
        ),
    ]
