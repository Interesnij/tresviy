# Generated by Django 2.2.5 on 2019-11-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20191130_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcommentvotes',
            name='vote',
            field=models.IntegerField(choices=[(-1, 'Не нравится'), (1, 'Нравится')], verbose_name='Голос'),
        ),
    ]
