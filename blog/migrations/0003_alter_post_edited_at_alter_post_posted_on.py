# Generated by Django 4.2.2 on 2023-10-24 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='edited_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]