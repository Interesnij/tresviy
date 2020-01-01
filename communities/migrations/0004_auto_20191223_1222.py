# Generated by Django 2.2.5 on 2019-12-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0003_auto_20191223_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='community',
            name='rules',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Правила'),
        ),
    ]
