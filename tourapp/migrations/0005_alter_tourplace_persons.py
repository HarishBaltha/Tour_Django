# Generated by Django 3.2.5 on 2021-07-29 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0004_adminmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourplace',
            name='Persons',
            field=models.CharField(max_length=100),
        ),
    ]
