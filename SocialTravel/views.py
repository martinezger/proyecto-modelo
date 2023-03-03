from django.shortcuts import render
from SocialTravel.models import Post

def index(request):
    return render(request, "SocialTravel/index.html")


def mostrar_otro_template(request):
    posts = Post.objects.all()
    return render(request, "SocialTravel/otro_template.html", {"posts": posts})