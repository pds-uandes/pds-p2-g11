# Generated by Django 4.2.5 on 2023-09-24 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_alter_dinamicanswer_question_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="dinamicanswer",
            name="result",
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
