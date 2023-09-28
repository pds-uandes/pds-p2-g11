# Generated by Django 4.2.5 on 2023-09-28 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_customuser_json_user_customuser_user_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='last_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_last_task', to='home.task'),
        ),
        migrations.AddField(
            model_name='dinamicanswer',
            name='hint',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]