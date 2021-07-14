from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Profile,Post,Comment,Follow
from .forms import PostForm, CreateUserForm, UpdateProfileForm, UserCommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='login')
def index(request):
    posts=Post.objects.all()
    return render(request, 'index.html', {"posts":posts})

@login_required(login_url='login')
def upload_image(request):
    users  = User.objects.all()
    posts = Post.objects.all()
    form = PostForm(request.POST or None, files=request.FILES)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user.profile
        post.save()
        return redirect('index')
    context = {
        'posts': posts,
        'form' : form,
        'users' :users,
    }
    return render(request,'new_post.html',{"form":form})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
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
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    images = request.user.profile.posts.all()
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(request.path_info)
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {"images":images,"profile_form" :profile_form})

# @login_required(login_url='login')
# def update_profile(request):  
#   if request.method=='POST':
#     user_form=UserUpdateForm(request.POST, instance=request.user)
#     profile_form=UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

#     if user_form.is_valid() and profile_form.is_valid():
#       user_form.save()
#       profile_form.save()            
#       return redirect("profile")
#   else:
#     user_form=UserUpdateForm(instance=request.user)
#     profile_form=UpdateProfileForm(instance=request.user.userprofile)

#   context={
#     'user_form':user_form,
#     'profile_form':profile_form,
#   } 

#   return render(request,'updateprofile.html',context)  

@login_required(login_url='login')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_name = request.GET.get("user")
        searched_profiles = Profile.search_profile(search_name)
        message = f"{search_name}"

        return render(request,"search.html",{"message":message,"searched_profiles":searched_profiles})
    else:
        message = "Enter name to search"
        return render(request,"search.html",{"message":message})

def comment(request, id):
    all_comments = Comment.get_comments(id)
    image = get_object_or_404(Post, id=id)
    form = UserCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = image
        comment.user = request.user.profile
        comment.save()
        return HttpResponseRedirect(request.path_info)
    else:
        form = UserCommentForm()
    return render(request, 'comments.html', {"comments":all_comments})






    










