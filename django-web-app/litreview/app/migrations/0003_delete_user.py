# Generated by Django 4.0.1 on 2022-01-11 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
