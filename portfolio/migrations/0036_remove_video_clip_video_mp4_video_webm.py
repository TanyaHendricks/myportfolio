# Generated by Django 4.0.1 on 2022-01-10 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0035_rename_video_video_clip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='clip',
        ),
        migrations.AddField(
            model_name='video',
            name='mp4',
            field=models.FileField(default='Default.png', upload_to='video'),
        ),
        migrations.AddField(
            model_name='video',
            name='webm',
            field=models.FileField(default='Default.png', upload_to='video'),
        ),
    ]
