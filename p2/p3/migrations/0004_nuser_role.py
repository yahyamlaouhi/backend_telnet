# Generated by Django 4.0.1 on 2022-02-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p3', '0003_remove_nuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='nuser',
            name='Role',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
