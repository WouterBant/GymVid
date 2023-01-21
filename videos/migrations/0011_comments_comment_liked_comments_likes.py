# Generated by Django 4.1.3 on 2022-12-01 09:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0010_subscribers'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_liked',
            field=models.ManyToManyField(blank=True, related_name='comment_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comments',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]