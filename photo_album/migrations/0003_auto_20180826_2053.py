# Generated by Django 2.0.6 on 2018-08-26 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo_album', '0002_auto_20180824_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='photo_album.Album'),
        ),
    ]
