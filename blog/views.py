

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def bloghome(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request,'blog/bloghome.html',context)


def blogPost(request,slug):
    post  = Post.objects.filter(slug=slug).first() #can also write [0] instead of .firts()
    context = {'post':post}
   

    return render(request,'blog/blogpost.html',context)



