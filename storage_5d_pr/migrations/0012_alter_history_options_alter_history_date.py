# Generated by Django 4.1.5 on 2023-01-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_5d_pr', '0011_alter_history_construction_alter_history_workers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data'),
        ),
    ]
