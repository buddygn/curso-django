# Generated by Django 4.0.1 on 2022-01-21 02:06

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0009_aula_teste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='teste',
            field=django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=8, unique=True),
        ),
    ]
