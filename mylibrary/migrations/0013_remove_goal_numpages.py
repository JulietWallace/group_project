# Generated by Django 2.2 on 2024-03-14 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0012_auto_20240314_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='numPages',
        ),
    ]
