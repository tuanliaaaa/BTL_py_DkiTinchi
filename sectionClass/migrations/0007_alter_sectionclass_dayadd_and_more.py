# Generated by Django 4.1 on 2022-11-21 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectionClass', '0006_sectionclass_termmajorsubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionclass',
            name='dayAdd',
            field=models.CharField(max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='sectionclass',
            name='dayLessonList',
            field=models.CharField(max_length=100000, null=True),
        ),
    ]
