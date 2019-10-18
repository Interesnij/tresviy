# Generated by Django 2.2.5 on 2019-10-17 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20191016_1211'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='articlecommentmute',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='articlecommentmute',
            name='article_comment',
        ),
        migrations.RemoveField(
            model_name='articlecommentmute',
            name='muter',
        ),
        migrations.AlterUniqueTogether(
            name='articlecommentusermention',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='articlecommentusermention',
            name='article_comment',
        ),
        migrations.RemoveField(
            model_name='articlecommentusermention',
            name='user',
        ),
        migrations.RemoveField(
            model_name='article',
            name='uuid',
        ),
        migrations.DeleteModel(
            name='ArticleComment',
        ),
        migrations.DeleteModel(
            name='ArticleCommentMute',
        ),
        migrations.DeleteModel(
            name='ArticleCommentUserMention',
        ),
    ]
