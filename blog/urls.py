from django.urls import path
from django.http import HttpResponse
from . import views


def _fallback(request):
    return HttpResponse("Blog home placeholder")


blog_home_view = getattr(views, 'PostListView', None)
if blog_home_view and hasattr(blog_home_view, 'as_view'):
    blog_home_view = blog_home_view.as_view()
else:
    blog_home_view = getattr(views, 'home', _fallback)


urlpatterns = [
    path('', blog_home_view, name='blog_list'),
]
