# Generated by Django 4.0.1 on 2022-07-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticket", "0002_alter_review_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
