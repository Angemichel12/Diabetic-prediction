# Generated by Django 4.1.5 on 2023-01-17 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prediction", "0011_predictiontable_hey_alter_predictiontable_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="predictiontable", name="hey",),
        migrations.AlterField(
            model_name="predictiontable",
            name="Age",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Delaed_healing",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Excessive_eating",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Excessive_thirst",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Hair_loss",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Irritability",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Itching",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Muscle_stiffiness",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Obesity",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Partial_paresis",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Sex",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Sudden_Weight_loss",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Visual_blurring",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Weakness",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="predictiontable",
            name="Yeast_infection",
            field=models.CharField(max_length=100),
        ),
    ]
