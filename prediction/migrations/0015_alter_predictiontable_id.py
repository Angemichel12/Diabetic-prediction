# Generated by Django 4.1.5 on 2023-01-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prediction", "0014_alter_predictiontable_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predictiontable",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
