# Generated by Django 4.0.1 on 2022-01-14 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0040_alter_experience_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='mp4',
        ),
    ]
