from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from posts.models import Post
from django.urls import path, re_path,reverse
from . import views

urlpatterns = [
                path('', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-updated")[:25],
                                    template_name="posts/index.html"), name= "posts"),
                path('<int:pk>/', DetailView.as_view(
                                    model = Post,
                                    template_name="posts/post.html") , name='posts-post-detail'),
                path('tag/<tag>', views.tagpage, name="tagpage"),
                path('resume', views.resume, name='resume'),
                # path('<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
               ]
