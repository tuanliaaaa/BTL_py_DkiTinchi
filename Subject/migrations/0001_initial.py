# Generated by Django 4.1 on 2022-10-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SubjectCode', models.CharField(max_length=255)),
                ('SubjectName', models.CharField(max_length=255)),
                ('semester', models.FloatField()),
                ('numberOfCredits', models.IntegerField()),
            ],
        ),
    ]
