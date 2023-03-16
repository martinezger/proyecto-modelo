from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    carousel_caption_title = models.CharField(max_length=30)
    carousel_caption_description = models.CharField(max_length=80)
    heading = models.CharField(max_length=15)
    description = models.CharField(max_length=120)
    un_campo = models.CharField(max_length=10)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="publisher") 
    image = models.ImageField(upload_to="posts", null=True, blank=True)

    @property
    def image_url(self):
        return self.image.url if self.image else ''

    def __str__(self):
        return f"{self.id} - {self.carousel_caption_title} - {self.publisher.username}"


class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="avatar")
    image = models.ImageField(upload_to="avatares", null=True, blank=True)
