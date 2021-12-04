# Generated by Django 3.2.9 on 2021-12-04 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20211204_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='image',
            field=models.ImageField(default='Default_Institute.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='institution',
            name='logo',
            field=models.ImageField(blank=True, default='Default_Institute.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='website',
            name='image',
            field=models.ImageField(default='Default_Interest.png', upload_to=''),
        ),
    ]