# Generated by Django 2.2.5 on 2019-09-16 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='communities',
            field=models.ManyToManyField(blank=True, related_name='categories', to='communities.Community', verbose_name='Сообщество'),
        ),
        migrations.AddField(
            model_name='category',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_categories', to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
    ]
