# Generated by Django 4.1 on 2022-11-05 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('majorName', models.CharField(max_length=255)),
                ('majorCode', models.CharField(max_length=255)),
            ],
        ),
    ]