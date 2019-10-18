# Generated by Django 2.2.5 on 2019-10-18 19:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModeratedObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='Описание')),
                ('verified', models.BooleanField(default=False, verbose_name='Одобрено')),
                ('status', models.CharField(choices=[('P', 'На рассмотрении'), ('A', 'Одобренный'), ('R', 'Отвергнутый')], default='P', max_length=5, verbose_name='Статус')),
                ('object_type', models.CharField(choices=[('P', 'Запись'), ('PC', 'Комментарий к запись'), ('C', 'Сообщество'), ('U', 'Пользователь'), ('A', 'Статья'), ('AC', 'Комментарий к статье'), ('G', 'Товар'), ('GC', 'Комментарий к товару')], max_length=5, verbose_name='Тип модерируемого объекта')),
                ('object_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectDescriptionChangedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_from', models.CharField(max_length=100, null=True, verbose_name='От')),
                ('changed_to', models.CharField(max_length=100, null=True, verbose_name='До')),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectStatusChangedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_from', models.CharField(choices=[('P', 'На рассмотрении'), ('A', 'Одобренный'), ('R', 'Отвергнутый')], max_length=5, verbose_name='От')),
                ('changed_to', models.CharField(max_length=5, verbose_name='До')),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectVerifiedChangedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_from', models.BooleanField(verbose_name='От')),
                ('changed_to', models.BooleanField(verbose_name='До')),
            ],
        ),
        migrations.CreateModel(
            name='ModerationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('title', models.CharField(max_length=64, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Создано')),
                ('order', models.PositiveIntegerField(editable=False, verbose_name='Порядковый номер')),
                ('severity', models.CharField(choices=[('C', 'Критический'), ('H', 'Высокий'), ('M', 'Средний'), ('L', 'Низкий')], max_length=5, verbose_name='Строгость')),
            ],
        ),
        migrations.CreateModel(
            name='ModerationReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='moderation.ModerationCategory', verbose_name='Категория')),
                ('moderated_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='moderation.ModeratedObject', verbose_name='Объект')),
            ],
        ),
        migrations.CreateModel(
            name='ModerationPenalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration', models.DateTimeField(null=True, verbose_name='Окончание')),
                ('type', models.CharField(choices=[('S', 'Приостановлено')], max_length=5, verbose_name='Тип')),
                ('moderated_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_penalties', to='moderation.ModeratedObject', verbose_name='Объект')),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_type', models.CharField(choices=[('DC', 'Описание Изменено'), ('AC', 'Статус Изменился'), ('VC', 'Проверка Изменена'), ('CC', 'Категория изменена')], max_length=5, verbose_name='Тип')),
                ('object_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='Создан')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('moderated_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='moderation.ModeratedObject', verbose_name='Объект')),
            ],
        ),
        migrations.CreateModel(
            name='ModeratedObjectCategoryChangedLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changed_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='moderation.ModerationCategory', verbose_name='От')),
                ('changed_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='moderation.ModerationCategory', verbose_name='До')),
            ],
        ),
        migrations.AddField(
            model_name='moderatedobject',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderated_objects', to='moderation.ModerationCategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='moderatedobject',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddConstraint(
            model_name='moderationreport',
            constraint=models.UniqueConstraint(fields=('reporter', 'moderated_object'), name='reporter_moderated_object_constraints'),
        ),
        migrations.AddConstraint(
            model_name='moderatedobject',
            constraint=models.UniqueConstraint(fields=('object_type', 'object_id'), name='reporter_moderated_object_constraint'),
        ),
    ]
