from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'registration/signup.html', {'form': form})

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
def user_login(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)

        messages.success(
            request,
            f" Welcome back, {user.username}!"
        )

        return redirect('/')

    return render(request, 'registration/login.html', {'form': form})

