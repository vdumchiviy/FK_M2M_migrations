# Generated by Django 3.1.4 on 2021-02-14 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20210213_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='student',
        ),
    ]
