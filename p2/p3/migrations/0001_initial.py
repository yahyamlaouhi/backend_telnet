# Generated by Django 4.0.2 on 2022-02-05 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomPrenom', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Pwd1', models.CharField(max_length=50)),
                ('Pwd2', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=1)),
                ('Department', models.CharField(max_length=50)),
                ('Role', models.CharField(max_length=50)),
                ('MartialStatus', models.CharField(max_length=50)),
            ],
        ),
    ]
