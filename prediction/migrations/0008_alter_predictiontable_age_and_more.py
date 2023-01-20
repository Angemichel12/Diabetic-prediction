# Generated by Django 4.1.5 on 2023-01-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prediction", "0007_alter_predictiontable_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="predictiontable",
            name="Age",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Delaed_healing",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Excessive_eating",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Excessive_thirst",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Excessive_urine",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Hair_loss",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Irritability",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Itching",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Muscle_stiffiness",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Obesity",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Partial_paresis",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Sex",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Sudden_Weight_loss",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Visual_blurring",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Weakness",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Yeast_infection",
            field=models.PositiveIntegerField(),
        ),
    ]
