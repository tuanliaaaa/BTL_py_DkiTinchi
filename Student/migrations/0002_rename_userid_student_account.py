# Generated by Django 4.1 on 2022-11-05 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='userID',
            new_name='account',
        ),
    ]
