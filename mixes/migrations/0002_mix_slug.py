# Generated by Django 4.2.2 on 2023-06-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mix',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]