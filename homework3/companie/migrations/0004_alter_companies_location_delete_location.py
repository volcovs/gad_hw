# Generated by Django 5.0.1 on 2024-01-26 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companie', '0003_companies_location'),
        ('locatie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locatie.location'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
