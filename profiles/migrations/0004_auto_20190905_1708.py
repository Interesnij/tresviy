# Generated by Django 2.2.5 on 2019-09-05 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_userprofile_badges'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_activity',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Активность'),
        ),
    ]
