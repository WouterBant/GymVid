# Generated by Django 4.1.3 on 2022-12-01 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_comments_comment_liked_comments_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='time_posted',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='videos_posted',
            name='time_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
