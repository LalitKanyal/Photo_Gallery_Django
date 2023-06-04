from django.shortcuts import render
from .models import Album, Photos
from django.db.models import Count
# showing dashboard after login
from django.contrib.auth.decorators import login_required

# User SignUp
from django.contrib.auth.forms import UserCreationForm

def home(request):
    data=Album.objects.annotate(total_photos=Count('photos')).all()
    return render(request, 'home.html', {'data':data})

# Photos
def photos(request, album_id):
    album = Album.objects.get(id=album_id)
    data=Photos.objects.filter(album=album)
    return render(request, 'photos.html', {'data':data, 'album':album})

# SignUp
def signup(request):
	msg=''
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			msg='Thanks for signup'
	form=UserCreationForm
	return render(request, 'registration/signup.html',{'form':form,'msg':msg})

# Dashboard
@login_required
def dashboard(request):
	totalAlbums=Album.objects.filter(user=request.user).count()
	totalPhotos=Photos.objects.filter(album__user=request.user).count()
	return render(request, 'dashboard.html', {'totalAlbums':totalAlbums, 'totalPhotos':totalPhotos})

# User Albums
@login_required
def user_albums(request):
    data=Album.objects.annotate(total_photos=Count('photos')).all()
    return render(request, 'user-albums.html', {'data':data})
    

