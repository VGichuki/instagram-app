from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,Post,Comment,Follow
from .forms import PostForm

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




