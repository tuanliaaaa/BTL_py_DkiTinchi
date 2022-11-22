# Generated by Django 4.1 on 2022-11-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termName', models.CharField(max_length=255)),
                ('StartTimeSignTerm', models.DateTimeField()),
                ('EndTimeSignTerm', models.DateTimeField()),
                ('StartTimeSignSubject', models.DateTimeField()),
                ('EndTimeSignSubject', models.DateTimeField()),
            ],
        ),
    ]
