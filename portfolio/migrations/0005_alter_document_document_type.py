# Generated by Django 3.2.9 on 2021-12-04 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20211204_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='portfolio.documenttype'),
        ),
    ]
