# Generated by Django 4.1 on 2022-11-05 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SubjectMajor', '0001_initial'),
        ('sectionClass', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionclass',
            name='subjectID',
        ),
        migrations.AddField(
            model_name='sectionclass',
            name='subjectMajor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SubjectMajor.subjectmajor'),
        ),
    ]
