from django.contrib import admin
from .models import Artiste, Song, Lyric

# Register your models here.
class SongItemInline(admin.TabularInline):
    model = Song
    raw_id_fields = ['artiste']


class ArtisteAdmin(admin.ModelAdmin):
    search_fields = ['id', 'first_name', 'last_name', 'age']
    list_display = ['first_name', 'last_name', 'age']
    inlines = [SongItemInline]


class SongAdmin(admin.ModelAdmin):
    search_fields = ['artiste', 'name', 'released_date', 'likes']
    list_display = ['name', 'artiste', 'released_date', 'likes']


class LyricAdmin(admin.ModelAdmin):
    search_fields = ['song_id', 'artiste']
    list_display = ['song_id', 'artiste']
    

admin.site.register (Artiste, ArtisteAdmin)
admin.site.register (Song, SongAdmin)
admin.site.register (Lyric, LyricAdmin)
