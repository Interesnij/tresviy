# Generated by Django 2.2.5 on 2019-09-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('profiles', '0002_remove_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='badges',
            field=models.ManyToManyField(related_name='users_profiles', to='common.Badge', verbose_name='Значки'),
        ),
    ]
