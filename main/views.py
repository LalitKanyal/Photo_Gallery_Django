from django.shortcuts import render
from .models import Album
from django.db.models import Count

def home(request):
    data=Album.objects.annotate(total_photos=Count('photos')).all()
    return render(request, 'home.html', {'data':data})