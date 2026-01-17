from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Testimonial
from .forms import TestimonialForm

@login_required
def testimonial_list(request):
    testimonials = Testimonial.objects.filter(approved=True)
    return render(request, 'testimonials/list.html', {'testimonials': testimonials})

@login_required
def testimonial_create(request):
    form = TestimonialForm(request.POST or None)
    if form.is_valid():
        t = form.save(commit=False)
        t.user = request.user
        t.save()
        return redirect('testimonial_list')
    return render(request, 'testimonials/form.html', {'form': form})

@login_required
def testimonial_edit(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk, user=request.user)
    form = TestimonialForm(request.POST or None, instance=testimonial)
    if form.is_valid():
        form.save()
        return redirect('testimonial_list')
    return render(request, 'testimonials/form.html', {'form': form})

@login_required
def testimonial_delete(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk, user=request.user)
    testimonial.delete()
    return redirect('testimonial_list')
