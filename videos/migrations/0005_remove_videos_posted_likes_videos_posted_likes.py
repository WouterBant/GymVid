# Generated by Django 4.1.3 on 2022-11-22 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_alter_videos_posted_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos_posted',
            name='likes',
        ),
        migrations.AddField(
            model_name='videos_posted',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]