# Generated by Django 4.1 on 2022-11-05 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Major', '0001_initial'),
        ('Subject', '0002_remove_subject_numberofcredits_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectMajor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfCredits', models.IntegerField()),
                ('startTerm', models.IntegerField()),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Major.major')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subject.subject')),
            ],
        ),
    ]
