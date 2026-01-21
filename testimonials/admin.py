from django.contrib import admin
from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'approved', 'created']
    list_filter = ['approved', 'created', 'rating']
    search_fields = ['user__username', 'content']
    list_editable = ['approved']
    readonly_fields = ['user', 'created']
