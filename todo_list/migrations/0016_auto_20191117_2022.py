# Generated by Django 2.2.7 on 2019-11-17 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0015_auto_20191117_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='due_date_input',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 18, 20, 22, 38, 849304), null=True),
        ),
    ]
