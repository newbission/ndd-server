# Generated by Django 5.0.6 on 2024-06-03 15:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_rename_conut_count"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Count",
        ),
    ]
