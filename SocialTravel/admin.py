from django.contrib import admin
from SocialTravel.models import Post, Profile

admin.site.register(Post)
admin.site.register(Profile)


# python manage.py createsuperuser --username admin