# Generated by Django 2.2.5 on 2019-09-16 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('frends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connect',
            name='target_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='targeted_connections', to=settings.AUTH_USER_MODEL, verbose_name='Кого переводит из подписчика в друзья'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connect',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='connections', to=settings.AUTH_USER_MODEL, verbose_name='Инициатор перевода из подписчика в друзья'),
            preserve_default=False,
        ),
    ]
