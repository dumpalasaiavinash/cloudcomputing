# Generated by Django 2.1.2 on 2018-11-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0009_merge_20181116_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='rating',
            field=models.IntegerField(default='5'),
        ),
    ]