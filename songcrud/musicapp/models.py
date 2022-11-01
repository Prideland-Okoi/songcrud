from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    Artiste=models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    date_released = models.CharField(max_length=50, null=True)
    likes = models.PositiveIntegerField()
    artist_id = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    Song=models.OneToOneField(Song, on_delete=models.CASCADE, primary_key=True)
    content = models.TextField()
    song_id = models.PositiveIntegerField()

class Musiclover(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Full_Name = models.CharField(max_length=50, null=True)
    Phone_Number = models.IntegerField(null=True)
    Country_Code = models.IntegerField(null=True)
    Email = models.EmailField(unique=True, null=True)
    Password = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.Email)

class ContactModel(models.Model):
    fl_name = models.CharField(max_length=100, null=True)
    email_address = models.EmailField(max_length = 150)
    subject_title = models.TextField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.fl-fl_name
class Subscribers(models.Model):
    #firstname = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

class AdminMailMessage(models.Model):
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    def __str__(self):
        return self.title
