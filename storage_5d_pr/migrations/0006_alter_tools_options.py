# Generated by Django 4.1.5 on 2023-01-17 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage_5d_pr', '0005_alter_tools_nr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tools',
            options={'ordering': ['nr']},
        ),
    ]
