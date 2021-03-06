# Generated by Django 3.1.6 on 2021-04-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20210409_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='averageRating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='thoughts',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
