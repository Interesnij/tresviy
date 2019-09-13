# Generated by Django 2.2.5 on 2019-09-12 15:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0004_auto_20190912_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='banned_users',
            field=models.ManyToManyField(blank=True, related_name='banned_of_communities', to=settings.AUTH_USER_MODEL, verbose_name='Черный список'),
        ),
        migrations.AlterField(
            model_name='community',
            name='starrers',
            field=models.ManyToManyField(blank=True, related_name='favorite_communities', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики'),
        ),
    ]
