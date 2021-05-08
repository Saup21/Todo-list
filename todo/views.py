from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def todo(request):
    if request.user.is_authenticated:
        return render(request, 'todo/todo.html', {})
    else:
        return redirect('login')
# def login_request(request):
#     # errors = ''
#     if request.method == 'POST':
#         # form = LoginForm(request, request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.info(request, 'Logged in successfully')
#             return redirect('/')
#         else:
#             messages.error(request, 'Invalid username or password')
#             # errors = 'Invalid username or password'
#             # errors = 'Invalid username or password'
#     # form = LoginForm()
#     # print(messages.error)
#     return render(request, 'todo/login.html', {})
def logout_request(request):
    logout(request)
    # messages.info(request, 'Logged out successfully')
    return redirect('/')
def register_request(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.info(request, 'Account created successfully')
        return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'todo/register.html', {'form': form})
