# Generated by Django 4.0.1 on 2022-01-14 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0004_auto_20220113_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(max_length=64, unique=True),
        ),
    ]
