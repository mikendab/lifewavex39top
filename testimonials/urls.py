from django.urls import path
from . import views

urlpatterns = [
    path('', views.testimonial_list, name='testimonial_list'),
    path('create/', views.testimonial_create, name='testimonial_create'),
    path('<int:pk>/edit/', views.testimonial_edit, name='testimonial_edit'),
    path('<int:pk>/delete/', views.testimonial_delete, name='testimonial_delete'),
]
