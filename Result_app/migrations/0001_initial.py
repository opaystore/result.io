# Generated by Django 4.2.13 on 2024-05-17 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('course_code', models.CharField(max_length=500)),
                ('course_unit', models.CharField(max_length=500)),
                ('level', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('total_course_unit', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('level', models.CharField(max_length=500)),
                ('registration_number', models.CharField(max_length=500)),
                ('department', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.FloatField()),
                ('grade', models.CharField(blank=True, max_length=20, null=True)),
                ('total_mark', models.FloatField()),
                ('remark', models.CharField(blank=True, max_length=200, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Result_app.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Result_app.semester')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Result_app.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Result_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, max_length=20, null=True)),
                ('score', models.FloatField()),
                ('remark', models.CharField(blank=True, max_length=200, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Result_app.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Result_app.semester')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Result_app.session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Result_app.student')),
            ],
        ),
    ]
