from django.db import models
from embed_video.fields import EmbedVideoField


class Mix(models.Model):

    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, unique=True, default="")
    image = models.ImageField(
        upload_to='images/', blank=False
    )
    content = models.TextField(blank=False)
    audio = EmbedVideoField(blank=True)
    draft = models.BooleanField()
    posted_on = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f'{self.id} {self.title}'
