# Generated by Django 2.2.7 on 2019-11-17 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0009_auto_20191117_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]