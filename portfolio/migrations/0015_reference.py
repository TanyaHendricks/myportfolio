# Generated by Django 3.2.9 on 2021-12-05 15:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_auto_20211205_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(default='Default.png', upload_to='')),
                ('url', models.URLField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
