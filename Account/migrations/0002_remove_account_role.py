# Generated by Django 4.1 on 2022-11-02 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='role',
        ),
    ]
