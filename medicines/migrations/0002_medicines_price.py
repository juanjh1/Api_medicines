# Generated by Django 4.1.6 on 2023-02-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medicines", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="medicines", name="price", field=models.IntegerField(default=1),
        ),
    ]