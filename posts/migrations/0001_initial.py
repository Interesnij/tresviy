# Generated by Django 2.2.5 on 2019-11-30 13:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('item_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.Item')),
                ('text', models.TextField(max_length=5000, null=True, verbose_name='Текст')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
            },
            bases=('main.item',),
        ),
        migrations.CreateModel(
            name='PostUserMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_mentions', to='posts.Post', verbose_name='Запись')),
                ('user', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='post_mentions', to=settings.AUTH_USER_MODEL, verbose_name='Упоминаемый')),
            ],
        ),
        migrations.CreateModel(
            name='PostDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to=posts.helpers.upload_to_post_directory, verbose_name='Документ')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_doc', to='posts.Post', verbose_name='Документ')),
            ],
        ),
    ]
