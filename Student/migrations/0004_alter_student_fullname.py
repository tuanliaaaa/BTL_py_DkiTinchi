# Generated by Django 4.1 on 2022-11-12 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_student_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fullName',
            field=models.CharField(max_length=255),
        ),
    ]