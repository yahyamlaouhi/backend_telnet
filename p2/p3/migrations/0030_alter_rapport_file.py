# Generated by Django 3.2.6 on 2022-07-31 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p3', '0029_auto_20220731_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapport',
            name='file',
            field=models.TextField(blank=True, null=True),
        ),
    ]