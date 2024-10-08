# Generated by Django 5.0.6 on 2024-08-05 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manytomanyapp', '0003_delete_course_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField()),
                ('final_grade', models.CharField(blank=True, max_length=1, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manytomanyapp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manytomanyapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='student',
            field=models.ManyToManyField(through='manytomanyapp.Enrollment', to='manytomanyapp.student'),
        ),
    ]
