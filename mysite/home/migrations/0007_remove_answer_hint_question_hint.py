# Generated by Django 4.2.5 on 2023-09-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_question_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='hint',
        ),
        migrations.AddField(
            model_name='question',
            name='hint',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
