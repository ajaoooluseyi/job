# Generated by Django 4.2.1 on 2023-07-31 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JobPosition",
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
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("skills", models.TextField()),
                (
                    "experience",
                    models.CharField(
                        choices=[
                            ("Fresher", "Fresher"),
                            ("Entry Level", "Entry Level"),
                            ("Intermediate", "Intermediate"),
                            ("Expert", "Expert"),
                        ],
                        max_length=20,
                    ),
                ),
                ("posted_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
