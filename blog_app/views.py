from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, UpdateForm


# def home(request):
#     return render(request, 'home.html', {})

class Home(ListView):
    model = Post
    template_name = 'home.html'

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
