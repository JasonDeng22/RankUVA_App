# Generated by Django 3.1.6 on 2021-05-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_review_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='date published'),
        ),
    ]
