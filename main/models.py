from django.db import models
from django.contrib.auth.models import User

# showing image in admin panel
from django.utils.safestring import mark_safe

#Album Model

class Album(models.Model):
    album_image = models.ImageField(upload_to="album_images/", null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = '1. Albums'

    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" height="100"/>' % (self.album_image.url))


# Photo Model

class Photos(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    image=models.ImageField(upload_to='photos/')
    alt_text=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '2. Photos'

    def __str__(self):
        return self.alt_text
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" height="100"/>' % (self.image.url))