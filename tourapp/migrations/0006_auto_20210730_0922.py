# Generated by Django 3.2.5 on 2021-07-30 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0005_alter_tourplace_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourplace',
            name='Place',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tourplace',
            name='slug',
            field=models.SlugField(),
        ),
    ]
