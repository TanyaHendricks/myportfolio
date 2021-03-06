# Generated by Django 3.2.9 on 2021-12-04 00:23

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_website_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='id',
            field=models.IntegerField(default=django.db.models.fields.AutoField, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='id',
            field=models.IntegerField(default=django.db.models.fields.AutoField, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='id',
            field=models.IntegerField(default=django.db.models.fields.AutoField, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='id',
            field=models.IntegerField(default=django.db.models.fields.AutoField, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='id',
            field=models.IntegerField(default=django.db.models.fields.AutoField, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
