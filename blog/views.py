from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import Post

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, 'blog/blog_detail.html', {'post': post})
