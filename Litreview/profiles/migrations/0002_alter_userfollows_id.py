# Generated by Django 4.0.1 on 2022-07-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfollows',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
