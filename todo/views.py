from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RegistrationForm, PostcreationForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def todo(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user).order_by('-published_date')
        return render(request, 'todo/todo.html', {'posts': posts})
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
def new_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostcreationForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.publish()
                return redirect('/')
        else:
            form = PostcreationForm()
        return render(request, 'todo/new_post.html', {'form': form})
    else:
        return redirect('login')
def post_detail(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, author=request.user, pk=pk)
        return render(request, 'todo/post_detail.html', {'post': post})
    else:
        return redirect('login')
