# Generated by Django 3.2.5 on 2021-07-30 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0010_auto_20210730_1252'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdminModel',
        ),
        migrations.DeleteModel(
            name='TourPlace',
        ),
    ]
