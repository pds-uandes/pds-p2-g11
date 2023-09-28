# Generated by Django 4.2.5 on 2023-09-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0015_alter_dinamicquestion_hint_alter_question_hint"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="json_user",
            field=models.JSONField(default={"difficulty": 1, "theme": 1}),
        ),
        migrations.AddField(
            model_name="customuser",
            name="user_score",
            field=models.JSONField(
                default={
                    "level1": {"correct": 0, "wrongs": 0},
                    "level2": {"correct": 0, "wrongs": 0},
                    "level3": {"correct": 0, "wrongs": 0},
                    "level4": {"correct": 0, "wrongs": 0},
                    "level5": {"correct": 0, "wrongs": 0},
                    "tasks": 0,
                }
            ),
        ),
        migrations.AlterField(
            model_name="dinamicquestion",
            name="theme",
            field=models.IntegerField(
                choices=[
                    (1, "Caracteristicas de la onda"),
                    (2, "Ondas Sonoras"),
                    (3, "Ondas Armonicas"),
                    (4, "Ecuacion de la Onda"),
                    (5, "Energias e Info. Transferida"),
                ],
                default=1,
            ),
        ),
    ]