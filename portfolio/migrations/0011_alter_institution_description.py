# Generated by Django 3.2.9 on 2021-12-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20211204_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
