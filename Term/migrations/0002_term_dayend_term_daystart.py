# Generated by Django 4.1 on 2022-11-29 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Term', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='term',
            name='dayEnd',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='term',
            name='dayStart',
            field=models.DateField(null=True),
        ),
    ]
