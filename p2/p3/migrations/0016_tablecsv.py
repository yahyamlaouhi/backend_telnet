# Generated by Django 4.0.1 on 2022-04-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p3', '0015_rename_myfiles_myuploadfile_myfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='tablecsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=50)),
                ('data', models.CharField(max_length=500)),
            ],
        ),
    ]
