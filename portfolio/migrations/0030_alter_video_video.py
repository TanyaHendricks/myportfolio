# Generated by Django 4.0.1 on 2022-01-10 09:31

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0029_alter_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]
