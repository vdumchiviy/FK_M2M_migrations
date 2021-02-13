# Generated by Django 3.1.4 on 2021-02-13 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_teacher_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherStudent',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='students', to='school.student', verbose_name='Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='teachers', to='school.teacher', verbose_name='Teacher')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='teacher',
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(
                related_name='students', through='school.TeacherStudent', to='school.Teacher'),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='student',
        ),
        migrations.AddField(
            model_name='teacher',
            name='student',
            field=models.ManyToManyField(
                related_name='teachers', through='school.TeacherStudent', to='school.Student'),
        ),
    ]