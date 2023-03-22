from django.contrib import admin
from SocialTravel.models import Post, Profile, Mensaje

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Mensaje)


# python manage.py createsuperuser --username admin