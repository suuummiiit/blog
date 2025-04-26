from django.urls import path
# from . import views
from .views import Home, ArticleDetails, Create_Post, Update_Post

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetails.as_view(), name="article_details"),
    path('create_post/', Create_Post.as_view(), name="create_post"),
    path('article/update/<int:pk>', Update_Post.as_view(), name="update_post"),
]