# Generated by Django 4.1.5 on 2023-01-24 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_5d_pr', '0021_alter_history_tool_nr_alter_history_tool_producer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='nr',
            field=models.CharField(max_length=8, unique=True, verbose_name='Nr ewidencyjny'),
        ),
    ]
