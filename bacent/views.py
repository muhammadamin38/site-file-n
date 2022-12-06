from django.shortcuts import render
from bacent.views import *
from .models import Post
from .models import TopPost

def home(request):
    posts = Post.objects.all()
    top = TopPost.objects.all()
    context = {
        'posts':posts,
        'Top':top
    }
    return render(request ,  'index.html', context)


 
