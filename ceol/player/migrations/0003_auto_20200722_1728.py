# Generated by Django 3.0.8 on 2020-07-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20200722_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='total_songs',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='total tracks'),
        ),
    ]