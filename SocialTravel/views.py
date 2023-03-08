from django.shortcuts import render
from SocialTravel.models import Post
from SocialTravel.forms import PostForm

def index(request):
    return render(request, "SocialTravel/index.html")


def mostrar_otro_template(request):
    posts = Post.objects.all()
    return render(request, "SocialTravel/otro_template.html", {"posts": posts})


def mostrar_post(request):

    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }

    return render(request, "SocialTravel/admin_post.html", context)


def agregar_post(request):
    post_form = PostForm(request.POST)
    post_form.save()
    
    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }

    return render(request, "SocialTravel/admin_post.html", context)

def buscar_post(request):
    criterio = request.GET.get("criterio")
    context = {
        "posts": Post.objects.filter(carousel_caption_title__icontains=criterio).all(),
    }

    return render(request, "SocialTravel/admin_post.html", context)