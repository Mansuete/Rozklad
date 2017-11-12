# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-23 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPanel', '0005_auto_20171023_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Створити розклад уроків',
                'verbose_name': 'Розклад уроків',
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_name', models.CharField(blank=True, default=None, max_length=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Навчальні тижні',
                'verbose_name': 'Навчальний тиждень',
            },
        ),
        migrations.RemoveField(
            model_name='dayingroup',
            name='day_name',
        ),
        migrations.RemoveField(
            model_name='dayingroup',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='lessoninday',
            name='day_name',
        ),
        migrations.RemoveField(
            model_name='lessoninday',
            name='lesson_number',
        ),
        migrations.AlterModelOptions(
            name='day',
            options={'verbose_name': 'Навчальний день', 'verbose_name_plural': 'Навчальнні дні'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Клас', 'verbose_name_plural': 'Класи'},
        ),
        migrations.AlterModelOptions(
            name='lessonname',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предмети'},
        ),
        migrations.AlterModelOptions(
            name='lessonnumber',
            options={'verbose_name': 'Номер уроку', 'verbose_name_plural': 'Номери уроків'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Номер Кабінета', 'verbose_name_plural': 'Номери Кабінетів'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Вчитель', 'verbose_name_plural': 'Вчителі'},
        ),
        migrations.RenameField(
            model_name='lessonnumber',
            old_name='number_lesson',
            new_name='lesson_number',
        ),
        migrations.RemoveField(
            model_name='day',
            name='name_day',
        ),
        migrations.RemoveField(
            model_name='lessonnumber',
            name='group_name',
        ),
        migrations.RemoveField(
            model_name='lessonnumber',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='lessonnumber',
            name='room',
        ),
        migrations.RemoveField(
            model_name='lessonnumber',
            name='teacher',
        ),
        migrations.AddField(
            model_name='day',
            name='day_name',
            field=models.CharField(blank=True, default=None, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='lessonname',
            name='lesson_name',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
        migrations.DeleteModel(
            name='DayInGroup',
        ),
        migrations.DeleteModel(
            name='LessonInDay',
        ),
        migrations.AddField(
            model_name='timetable',
            name='day',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.Day'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='group',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.Group'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='lesson_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.LessonName'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='lesson_number',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.LessonNumber'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='room_number',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.Room'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='teacher',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.Teacher'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='week',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.Week'),
        ),
    ]
