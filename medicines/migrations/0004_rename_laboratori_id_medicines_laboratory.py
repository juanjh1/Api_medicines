# Generated by Django 4.1.6 on 2023-02-04 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("medicines", "0003_medicines_laboratori_id_alter_medicines_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="medicines", old_name="laboratori_id", new_name="laboratory",
        ),
    ]