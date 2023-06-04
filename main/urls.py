from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('photos/<int:album_id>', views.photos, name='photos'),
	path('accounts/signup',views.signup,name='signup'),
	path('dashboard',views.dashboard,name='dashboard'),
    path('user-albums', views.user_albums,name='user-albums')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)