# Generated by Django 3.2.9 on 2022-01-07 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_auto_20211231_0319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='experience_id',
        ),
        migrations.AddField(
            model_name='experience',
            name='documents',
            field=models.ManyToManyField(blank=True, to='portfolio.Document'),
        ),
        migrations.AlterField(
            model_name='document',
            name='issued_id',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='commenced',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='completed',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='type',
            field=models.CharField(choices=[('Qualification', 'Qualification Experience'), ('Employment', 'Employment Experience'), ('Project', 'Project Experience'), ('Workshop', 'Workshop Experience'), ('Short Course', 'Short Course Experience')], default='', max_length=100),
        ),
    ]
