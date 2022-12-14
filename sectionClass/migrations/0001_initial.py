# Generated by Django 4.1 on 2022-10-18 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Subject', '0001_initial'),
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sectionClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayStart', models.DateField()),
                ('quanlity', models.IntegerField()),
                ('subjectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subject.subject')),
                ('teacherID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.teacher')),
            ],
        ),
    ]
