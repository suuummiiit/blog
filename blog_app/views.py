from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

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
    template_name = 'create_post.html'
    fields = '__all__'
    # fields = ('title', 'author', 'body')

