from django.shortcuts import render
from SocialTravel.models import Post
from SocialTravel.forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "SocialTravel/index.html")


class PostList(ListView):
    model = Post
    context_object_name = "posts"

class PostMineList(PostList):

    def get_queryset(self):
        return Post.objects.filter(publisher=self.request.user.id).all()

class PostDetail(DetailView):
    model = Post
    context_object_name = "post"


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = (
        'carousel_caption_title', 'carousel_caption_description',
        "heading", "description", "un_campo", "image",
        )

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Post.objects.filter(publisher=user_id,id=post_id).exists()


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = reverse_lazy("post-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Post.objects.filter(publisher=user_id,id=post_id).exists()


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = (
        'carousel_caption_title', 'carousel_caption_description',
        "heading", "description", "un_campo", "image",
        )

    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)


class PostSearch(ListView):
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Post.objects.filter(carousel_caption_title__icontains=criterio).all()
        return result

class Login(LoginView):
    next_page = reverse_lazy("index")


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('post-list')


class Logout(LogoutView):
    template_name = "registration/logout.html"