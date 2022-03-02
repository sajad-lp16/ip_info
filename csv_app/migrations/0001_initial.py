# Generated by Django 2.2.4 on 2022-02-27 07:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])], verbose_name='csv file')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'import csv file',
                'verbose_name_plural': 'import csv files',
                'db_table': 'csv_files',
            },
        ),
    ]