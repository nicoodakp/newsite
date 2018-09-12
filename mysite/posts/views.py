from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django import forms
from posts.models import Post
from django.urls import reverse

import django.http as http
import django.shortcuts as shortcuts
#
#



def tagpage(request, tag):
	posts = Post.objects.filter(tags__name=tag)
	return render_to_response("posts/tags.html", {"posts":posts, "tag":tag})


def posts_create(request):
	return HttpResponse("create")


def post_update(request):
	return HttpResponse("<h1>Update</h1>")


def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")

def resume(request):
    return render(request, 'posts/resume.html')
