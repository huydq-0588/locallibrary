# Generated by Django 3.2.19 on 2025-07-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre (e.g. Science Fiction,)', max_length=200),
        ),
    ]
