# Generated by Django 4.1 on 2022-11-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sectionClass', '0007_alter_sectionclass_dayadd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionclass',
            name='dayLessonList',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
    ]