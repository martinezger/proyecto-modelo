from django.contrib import admin
from SocialTravel.models import Post

admin.site.register(Post)


# python manage.py createsuperuser --username admin