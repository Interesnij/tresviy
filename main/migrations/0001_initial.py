# Generated by Django 2.2.5 on 2019-10-18 19:38

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.SmallIntegerField(choices=[(-1, 'Не нравится'), (1, 'Нравится')], verbose_name='Голос')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='uuid')),
                ('comments_enabled', models.BooleanField(default=True, verbose_name='Разрешить комментарии')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('is_edited', models.BooleanField(default=False, verbose_name='Изменено')),
                ('is_closed', models.BooleanField(default=False, verbose_name='Закрыто')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('is_fixed', models.BooleanField(default=False, verbose_name='Закреплено')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('creator', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('is_edited', models.BooleanField(default=False, verbose_name='Изменено')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удаено')),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Комментатор')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Item')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Comment', verbose_name='Родительский комментарий')),
            ],
        ),
        migrations.AddIndex(
            model_name='item',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='main_item_created_848de4_brin'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='main_commen_created_c5fc21_brin'),
        ),
    ]
