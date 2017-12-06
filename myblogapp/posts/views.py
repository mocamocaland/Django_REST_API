from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import django_filters
from rest_framework import viewsets, filters
from .models import Post
from .serializer import PostSerializer

# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer