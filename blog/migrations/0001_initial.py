# Generated by Django 4.2.2 on 2023-06-27 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
                ('audio_one', embed_video.fields.EmbedVideoField(blank=True)),
                ('audio_two', embed_video.fields.EmbedVideoField(blank=True)),
                ('audio_three', embed_video.fields.EmbedVideoField(blank=True)),
                ('audio_four', embed_video.fields.EmbedVideoField(blank=True)),
                ('audio_five', embed_video.fields.EmbedVideoField(blank=True)),
                ('draft', models.BooleanField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted_on'],
            },
        ),
    ]