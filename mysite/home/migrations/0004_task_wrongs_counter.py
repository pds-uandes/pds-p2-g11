# Generated by Django 4.2.5 on 2023-09-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_task_counter"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="wrongs_counter",
            field=models.IntegerField(default=0),
        ),
    ]
