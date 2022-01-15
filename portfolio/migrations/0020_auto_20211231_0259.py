# Generated by Django 3.2.9 on 2021-12-31 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_auto_20211231_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='issued_id',
            field=models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='commenced',
            field=models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='completed',
            field=models.DateTimeField(default=datetime.datetime(1900, 1, 1, 0, 0)),
        ),
    ]