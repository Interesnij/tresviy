# Generated by Django 2.2.5 on 2019-10-10 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191010_1709'),
        ('goods', '0004_auto_20191010_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='created',
        ),
        migrations.RemoveField(
            model_name='good',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='good',
            name='id',
        ),
        migrations.RemoveField(
            model_name='good',
            name='views',
        ),
        migrations.AddField(
            model_name='good',
            name='item_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Item'),
            preserve_default=False,
        ),
    ]
