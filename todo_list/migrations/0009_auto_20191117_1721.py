# Generated by Django 2.2.7 on 2019-11-17 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0008_auto_20191117_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='due_date',
            field=models.BooleanField(default=False),
        ),
    ]