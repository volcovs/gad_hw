# Generated by Django 5.0.1 on 2024-01-26 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companies',
            name='location',
        ),
    ]
