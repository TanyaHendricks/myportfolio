# Generated by Django 3.2.9 on 2022-01-08 18:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0028_auto_20220108_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
