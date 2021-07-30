# Generated by Django 3.2.5 on 2021-07-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourapp', '0012_adminmodel_tourplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30, unique=True)),
                ('Email', models.EmailField(max_length=20, unique=True)),
                ('Contact', models.IntegerField()),
                ('Address', models.CharField(blank=True, max_length=120, null=True)),
                ('Joined_on', models.DateTimeField(auto_now_add=True)),
                ('Password1', models.CharField(max_length=15, unique=True)),
                ('Password2', models.CharField(max_length=15)),
                ('Secret_Info', models.CharField(max_length=200)),
            ],
        ),
    ]