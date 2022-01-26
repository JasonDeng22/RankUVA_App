# Generated by Django 3.1.6 on 2021-04-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=1000)),
                ('x_coordinate', models.IntegerField(default=0)),
                ('y_coordinate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Thoughts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_field', models.CharField(max_length=1000)),
                ('id_field', models.CharField(max_length=1000)),
                ('text_field', models.TextField()),
                ('test', models.TextField()),
            ],
        ),
    ]