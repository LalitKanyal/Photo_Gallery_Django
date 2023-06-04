from django import forms
from . models import Album, Photos
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields=('title', 'album_image')