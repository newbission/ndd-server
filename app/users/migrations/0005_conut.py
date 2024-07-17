# Generated by Django 5.0.6 on 2024-06-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_remove_user_email_remove_user_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Conut",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("count", models.PositiveBigIntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
