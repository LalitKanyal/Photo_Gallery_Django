from django.shortcuts import render
from .models import Album, Photos
from django.db.models import Count

def home(request):
    data=Album.objects.annotate(total_photos=Count('photos')).all()
    return render(request, 'home.html', {'data':data})

# Photos
def photos(request, album_id):
    album = Album.objects.get(id=album_id)
    data=Photos.objects.filter(album=album)
    return render(request, 'photos.html', {'data':data, 'album':album})