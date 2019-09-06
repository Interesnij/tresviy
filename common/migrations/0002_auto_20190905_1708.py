# Generated by Django 2.2.5 on 2019-09-05 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='emoji',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создан'),
        ),
        migrations.AlterField(
            model_name='emojigroup',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Создана'),
        ),
    ]
