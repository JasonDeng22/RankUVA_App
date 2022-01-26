# Generated by Django 3.1.6 on 2021-04-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20210410_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='x_coordinate',
        ),
        migrations.RemoveField(
            model_name='location',
            name='y_coordinate',
        ),
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
