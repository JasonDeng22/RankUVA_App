# Generated by Django 3.1.6 on 2021-04-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_location_averagerating'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
        migrations.DeleteModel(
            name='Thoughts',
        ),
    ]
