from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import RegisterUserForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')
    else:
        return render(request, 'auth/login.html')


def logout(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered successfully')
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'auth/register.html', {'form': form})
