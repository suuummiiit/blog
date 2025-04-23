from django.urls import path
# from . import views
from .views import Home, ArticleDetails

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetails.as_view(), name="article_details"),

]