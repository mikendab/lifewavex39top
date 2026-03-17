from django.shortcuts import get_object_or_404, render
from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.filter(published=True).order_by('-created')
    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(request, 'blog/blog_detail.html', {'post': post})
