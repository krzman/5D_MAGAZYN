# Generated by Django 4.1.5 on 2023-01-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_5d_pr', '0004_alter_workers_options_alter_tools_construction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='nr',
            field=models.FloatField(max_length=16, unique=True, verbose_name='Nr ewidencyjny'),
        ),
    ]