# Generated by Django 4.1.5 on 2023-01-24 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prediction", "0015_alter_predictiontable_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="predictiontable",
            name="patient",
            field=models.CharField(default="admin", max_length=200),
        ),
    ]
