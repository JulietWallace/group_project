# Generated by Django 2.2 on 2024-03-14 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0011_auto_20240314_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='dateDay',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='dateMonth',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='dateYear',
        ),
    ]
