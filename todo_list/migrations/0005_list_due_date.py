# Generated by Django 2.2.7 on 2019-11-17 14:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_remove_list_due_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
