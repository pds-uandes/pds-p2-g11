# Generated by Django 4.2.5 on 2023-09-21 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="question_text",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="question_answer",
                to="home.question",
            ),
        ),
    ]