# Generated by Django 2.2.5 on 2019-11-30 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_auto_20191130_1403'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='community',
            field=models.ForeignKey(blank=True, db_index=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='communities.Community', verbose_name='Сообщество'),
        ),
    ]
