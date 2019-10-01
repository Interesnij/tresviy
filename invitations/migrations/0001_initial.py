# Generated by Django 2.2.5 on 2019-09-16 16:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Приглашение создано')),
                ('name', models.CharField(blank=True, max_length=35, null=True)),
                ('nickname', models.CharField(blank=True, max_length=35, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Емаил')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('is_invite_email_sent', models.BooleanField(default=False)),
                ('badge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Badge')),
            ],
        ),
    ]
