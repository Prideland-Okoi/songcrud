from django import forms
from . models import Artiste, Song, Lyric, ContactModel, Subscribers, AdminMailMessage

# Create your forms here.
class ArtisteForm(forms.ModelForm):
    class Meta:
        model = Artiste
        fields = ['first_name','last_name', 'age']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title','date_released']

#needs to link this count to the likes in song.models
#class LikeCounterForm(forms.Forms):
#    likes=forms.PositiveIntegerField()

class LyricForm(forms.ModelForm):
    class Meta:
        model = Lyric
        fields = '__all__'

class ContactForm(forms.Form):
    fl_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    subject_title = forms.CharField(widget = forms.Textarea, max_length = 100)
    message_detail = forms.CharField(widget = forms.Textarea, max_length = 2000)

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['firstname','email',]
        #fields ='__all__'

class AdminMailMessageForm(forms.ModelForm):
    class Meta:
        model = AdminMailMessage
        fields = '__all__'
