from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        messages.success(request, f'Account created successfully for {user.username}! Please log in.')
        return redirect('login')
    return render(request, 'registration/signup.html', {'form': form})

from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)

        messages.success(
            request,
            f"Welcome back, {user.username}!"
        )

        return redirect('/')

    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('/')
