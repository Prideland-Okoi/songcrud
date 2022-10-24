from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=50, null=True)
    date_released = models.CharField(max_length=50, null=True)
    likes = models.PositiveIntegerField()
    artist_id = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.PositiveIntegerField()
