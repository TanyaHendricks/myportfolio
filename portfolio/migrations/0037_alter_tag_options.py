# Generated by Django 4.0.1 on 2022-01-11 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0036_remove_video_clip_video_mp4_video_webm'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
    ]
