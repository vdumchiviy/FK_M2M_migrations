# Generated by Django 3.1.4 on 2021-02-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20210213_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(related_name='teachers', to='school.Student'),
        ),
    ]
