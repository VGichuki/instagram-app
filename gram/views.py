from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile,Post,Comment,Follow

# Create your views here.
def index(request):
    return render(request, 'index.html')


