# Generated by Django 4.1.3 on 2023-09-08 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="choice", name="votes",),
        migrations.AddField(
            model_name="choice",
            name="is_correct",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="question",
            name="difficulty",
            field=models.IntegerField(
                choices=[(1, "Easy"), (2, "Medium"), (3, "Hard")], default=1
            ),
        ),
    ]
