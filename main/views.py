from django.shortcuts import render, redirect
from .models import Album, Photos
from django.db.models import Count
# showing dashboard after login
from django.contrib.auth.decorators import login_required

# Form
from .forms import AlbumForm, PhotoForm

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
    data=Album.objects.annotate(total_photos=Count('photos')).filter(user=request.user)
    return render(request, 'user-albums.html', {'data':data})
    
@login_required
def add_album(request):
	msg=''
	if request.method=='POST':
		form=AlbumForm(request.POST,request.FILES)
		if form.is_valid():
			saveForm = form.save(commit=False)
			saveForm.user=request.user
			saveForm.save()
			msg='Album has been Added Successfully'
	form=AlbumForm
	return render(request, 'add-album.html',{'form':form,'msg':msg})

@login_required
def update_album(request,id):
	album=Album.objects.get(id=id)
	msg=''
	if request.method=='POST':
		form=AlbumForm(request.POST,request.FILES,instance=album)
		if form.is_valid():
			saveForm=form.save(commit=False)
			saveForm.user=request.user
			saveForm.save()
			msg='Data has been updated'
	form=AlbumForm(instance=album)
	return render(request, 'update-album.html',{'form':form,'msg':msg})

# Delete Album

@login_required
def delete_album(request, id):
	Album.objects.filter(id=id).delete()
	return redirect('user-albums')

# Photo List

@login_required
def photo_list(request, album_id):
	album=Album.objects.get(id=album_id)
	photos=Photos.objects.filter(album=album)
	return render(request, 'photo-list.html',{'data':photos, 'album':album})

# Add Photo
    
@login_required
def add_photo(request, album_id):
	album=Album.objects.get(id=album_id)
	msg=''
	if request.method=='POST':
		form=PhotoForm(request.user,request.POST,request.FILES)
		if form.is_valid():
			saveForm = form.save(commit=False)
			saveForm.save()
			msg='Photo has been Added Successfully'
			return redirect('/photo-list/'+str(album_id))
	form=PhotoForm(request.user)
	return render(request, 'add-photo.html',{'form':form,'msg':msg,'album':album})

# Delete Photo

@login_required
def delete_photo(request,album_id,photo_id):
	Photos.objects.filter(id=photo_id).delete()
	return redirect('/photo-list/'+str(album_id))