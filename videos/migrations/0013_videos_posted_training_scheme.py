# Generated by Django 4.1.3 on 2022-12-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_comments_time_posted_alter_videos_posted_time_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos_posted',
            name='training_scheme',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
