from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(req):
    # rs = HttpResponse()
    # rs.writelines("<h1>xin chao</h1>")
    # rs.write("day la home")
    # return rs
    return render(req,'pages/home.html')
def contact(req):
    return render(req, 'pages/contact.html')
def post(req):
    return render(req, 'pages/post.html')
def error(req,*args, **kwargs):
    return render(req, 'pages/error.html')
def register(req):
    form = RegistrationForm()
    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(req, 'pages/register.html',{'form':form})
