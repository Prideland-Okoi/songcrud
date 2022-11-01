from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Artiste(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    released_date = models.DateField(blank=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"


class Lyric(models.Model):
    content = HTMLField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.song_id}"
