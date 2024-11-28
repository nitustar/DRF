# Generated by Django 5.0.7 on 2024-11-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("price", models.IntegerField()),
                ("discount", models.IntegerField()),
                ("duration", models.FloatField()),
                ("author_name", models.CharField(max_length=100)),
            ],
        ),
    ]
