# Generated by Django 2.2.5 on 2019-11-01 14:19

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Item')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='articles/%Y/%m/%d', verbose_name='Главное изображение')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name': 'статья',
                'ordering': ['-created'],
                'verbose_name_plural': 'статьи',
            },
            bases=('main.item',),
        ),
    ]
