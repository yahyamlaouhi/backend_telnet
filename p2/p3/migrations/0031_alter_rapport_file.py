# Generated by Django 3.2.6 on 2022-07-31 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p3', '0030_alter_rapport_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapport',
            name='file',
            field=models.TextField(blank=True, default='text', null=True),
        ),
    ]
