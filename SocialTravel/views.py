from django.shortcuts import render
from SocialTravel.models import Post
from SocialTravel.forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


def index(request):
    return render(request, "SocialTravel/index.html")

class PostList(ListView): 
    model = Post

class PostDetail(DetailView):
    model = Post

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostSearch(ListView):
    model = Post
    
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = (Post.objects
        .filter(carousel_caption_title__icontains=criterio)
        .order_by("creado_el")
        .all())
        return result
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Resultados"
        return context