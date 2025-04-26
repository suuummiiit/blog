from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy


# def home(request):
#     return render(request, 'home.html', {})

class Home(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-post_datetime']

class ArticleDetails(DetailView):
    model = Post
    template_name = 'article_details.html'
    
class Create_Post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    # fields = '__all__'
    # fields = ('title', 'author', 'body')
    # PostForm now takes care of the fields

class Update_Post(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    # fields = ('title', 'body')

class Delete_Post(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')