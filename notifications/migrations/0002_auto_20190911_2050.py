# Generated by Django 2.2.5 on 2019-09-11 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0002_auto_20190911_2046'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityinvitenotification',
            name='community_invite',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='communities.CommunityInvite', verbose_name='Приглашение в сообщество'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connectionconfirmednotification',
            name='connection_confirmator',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Подтверждение заявки в друзья'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='connectionrequestnotification',
            name='connection_requester',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Запрос в друзья'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follownotification',
            name='follower',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Подписка'),
            preserve_default=False,
        ),
    ]
