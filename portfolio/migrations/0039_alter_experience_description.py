# Generated by Django 4.0.1 on 2022-01-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0038_alter_experience_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
