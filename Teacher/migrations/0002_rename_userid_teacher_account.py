# Generated by Django 4.1 on 2022-11-05 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='userID',
            new_name='account',
        ),
    ]