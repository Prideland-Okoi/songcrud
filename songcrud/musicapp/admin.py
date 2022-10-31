from django.contrib import admin
from .models import ContactModel, Musiclover, Subscribers, Artiste, Song, Lyric, AdminMailMessage

# Register your models here.
admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyric)
admin.site.register(ContactModel)
admin.site.register(Musiclover)
admin.site.register(Subscribers)
admin.site.register(AdminMailMessage)
