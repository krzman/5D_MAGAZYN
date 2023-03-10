# Generated by Django 4.1.5 on 2023-01-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_5d_pr', '0008_remove_construction_deleted_remove_tools_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='tool',
        ),
        migrations.AddField(
            model_name='history',
            name='tool_nr',
            field=models.FloatField(default=0.0, max_length=32, unique=True, verbose_name='Nr ew'),
        ),
        migrations.AddField(
            model_name='history',
            name='tool_producer',
            field=models.CharField(default=0, max_length=64, verbose_name='Marka'),
        ),
        migrations.AddField(
            model_name='history',
            name='tool_type',
            field=models.CharField(default=0, max_length=128, verbose_name='Typ'),
        ),
        migrations.AlterField(
            model_name='history',
            name='construction',
            field=models.CharField(max_length=64, verbose_name='Obiekt'),
        ),
        migrations.AlterField(
            model_name='history',
            name='user',
            field=models.CharField(max_length=64, verbose_name='Użytkownik'),
        ),
        migrations.AlterField(
            model_name='history',
            name='workers',
            field=models.CharField(max_length=64, verbose_name='Pracownik'),
        ),
    ]
