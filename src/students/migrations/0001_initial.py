# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='semester',
            name='student',
            field=models.ForeignKey(to='students.Student'),
        ),
        migrations.AddField(
            model_name='semester',
            name='student_class',
            field=models.ForeignKey(to='students.StudentClass'),
        ),
        migrations.AlterUniqueTogether(
            name='semester',
            unique_together=set([('student', 'student_class')]),
        ),
    ]
