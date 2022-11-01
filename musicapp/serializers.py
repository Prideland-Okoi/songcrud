from rest_framework import serializers
from .models import Artiste, Song, Lyric

class ArtisteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = '__all__'


class SongSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class LyricSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = '__all__'

#class DeleteArtisteSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Artiste
#        fields = '__all__'
#class UpdateSongSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Artiste
#        fields = '__all__'
