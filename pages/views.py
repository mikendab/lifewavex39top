from django.shortcuts import render

# Create your views here.
from blog.models import Post
from testimonials.models import Testimonial
from django.shortcuts import render

def home(request):
    blogs = Post.objects.filter(published=True)[:3]
    testimonials = Testimonial.objects.filter(approved=True)[:3]
    return render(request, 'pages/home.html', {
        'blogs': blogs,
        'testimonials': testimonials
    })
