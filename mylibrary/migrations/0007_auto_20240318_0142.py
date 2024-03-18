# Generated by Django 2.2.28 on 2024-03-18 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0006_auto_20240317_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='categories',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='mylibrary.Category'),
        ),
    ]