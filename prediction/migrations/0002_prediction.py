# Generated by Django 4.1.5 on 2023-01-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prediction", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prediction",
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
                ("n1", models.CharField(max_length=100)),
                ("n2", models.CharField(max_length=100)),
                ("n3", models.CharField(max_length=100)),
                ("n4", models.CharField(max_length=100)),
                ("n5", models.CharField(max_length=100)),
                ("n6", models.CharField(max_length=100)),
                ("n7", models.CharField(max_length=100)),
                ("n8", models.CharField(max_length=100)),
                ("n9", models.CharField(max_length=100)),
                ("n10", models.CharField(max_length=100)),
                ("n11", models.CharField(max_length=100)),
                ("n12", models.CharField(max_length=100)),
                ("n13", models.CharField(max_length=100)),
                ("n14", models.CharField(max_length=100)),
                ("n15", models.CharField(max_length=100)),
                ("n16", models.CharField(max_length=100)),
            ],
        ),
    ]
