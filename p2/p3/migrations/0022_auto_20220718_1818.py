# Generated by Django 3.2.6 on 2022-07-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p3', '0021_auto_20220718_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfile',
            name='file_encoded',
        ),
        migrations.AlterField(
            model_name='csvfile',
            name='file',
            field=models.FileField(upload_to='files/csv'),
        ),
    ]
