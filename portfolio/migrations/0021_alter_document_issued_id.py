# Generated by Django 3.2.9 on 2021-12-31 01:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0020_auto_20211231_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='issued_id',
            field=models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0, 1)),
        ),
    ]