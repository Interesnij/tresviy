# Generated by Django 2.2.5 on 2019-12-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='users', verbose_name='Фон'),
        ),
    ]
