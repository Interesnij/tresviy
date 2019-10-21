# Generated by Django 2.2.5 on 2019-10-19 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import goods.helpers
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер')),
                ('image', models.ImageField(blank=True, upload_to='goods/list', verbose_name='Изображение')),
            ],
            options={
                'ordering': ['order', 'name'],
                'verbose_name_plural': 'категории товаров',
                'verbose_name': 'категория товаров',
            },
        ),
        migrations.CreateModel(
            name='GoodSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название подкатегории')),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядковый номер подкатегории')),
                ('image', models.ImageField(blank=True, upload_to='sub_category/list', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodCategory', verbose_name='Категория-родитель')),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, verbose_name='uuid')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена товара')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание товара')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to="goods/%Y/%m/%d", verbose_name='Главное изображение')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('views', models.IntegerField(default=0, verbose_name='Просмотры')),
                ('creator', models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodSubCategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
    ]
