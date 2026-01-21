from django.urls import path
from .views import signup, user_logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]
