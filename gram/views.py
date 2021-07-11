from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Post,Comment,Follow
from .forms import PostForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request, 'index.html', {"posts":posts})

def upload_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('index')
    else:
        form = PostForm()
    return render(request,'new_post.html',{"form":form})

def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {"form" : form}
    return render(request, 'registration/register.html', context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('index')
    context = {}
    return render(request, 'registration/login.html')




