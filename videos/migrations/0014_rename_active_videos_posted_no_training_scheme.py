# Generated by Django 4.1.3 on 2022-12-06 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0013_videos_posted_training_scheme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos_posted',
            old_name='active',
            new_name='no_training_scheme',
        ),
    ]
