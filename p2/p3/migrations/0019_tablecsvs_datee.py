# Generated by Django 4.0.1 on 2022-04-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p3', '0018_tablecsvs'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablecsvs',
            name='datee',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
