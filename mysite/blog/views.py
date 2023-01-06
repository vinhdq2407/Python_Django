from django.shortcuts import render
from .models import Post
# Create your views here.

def list(req):
    Data = {'Posts' : Post.objects.all().order_by("-date")}
    return render(req,'blog/blog.html',Data)
def postById(req,id):
    post = Post.objects.get(id=id)
    return render(req,'blog/post.html',{'post':post})

