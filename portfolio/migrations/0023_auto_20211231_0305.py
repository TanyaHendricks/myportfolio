# Generated by Django 3.2.9 on 2021-12-31 01:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_auto_20211231_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='issued_id',
            field=models.DateTimeField(default=datetime.time(0, 0, 1)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='commenced',
            field=models.DateTimeField(default=datetime.time(0, 0, 1)),
        ),
        migrations.AlterField(
            model_name='experience',
            name='completed',
            field=models.DateTimeField(default=datetime.time(0, 0, 1)),
        ),
    ]
