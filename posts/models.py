from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    image = models.ImageField(
        upload_to='images/', blank=False
    )
    content = models.TextField(blank=False)
    audio_one = EmbedVideoField(blank=True)
    audio_two = EmbedVideoField(blank=True)
    audio_three = EmbedVideoField(blank=True)
    audio_four = EmbedVideoField(blank=True)
    audio_five = EmbedVideoField(blank=True)
    draft = models.BooleanField()
    posted_on = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f'{self.id} {self.title}'