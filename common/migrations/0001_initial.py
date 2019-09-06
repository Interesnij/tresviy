# Generated by Django 2.2.5 on 2019-09-03 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=16, unique=True, verbose_name='Слово')),
                ('keyword_description', models.CharField(blank=True, max_length=64, null=True, unique=True, verbose_name='Описание')),
                ('created', models.DateTimeField(editable=False, verbose_name='Создан')),
            ],
        ),
        migrations.CreateModel(
            name='EmojiGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=32, verbose_name='Слово')),
                ('order', models.IntegerField(default=100, verbose_name='Порядковый номер')),
                ('created', models.DateTimeField(editable=False, verbose_name='Создана')),
                ('is_reaction_group', models.BooleanField(default=False, verbose_name='Это реакция группы')),
            ],
        ),
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=16, verbose_name='Слово')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('created', models.DateTimeField(editable=False, verbose_name='Создан')),
                ('order', models.IntegerField(default=100, verbose_name='Порядковый номер')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='emojis', to='common.EmojiGroup', verbose_name='Группа')),
            ],
        ),
    ]
