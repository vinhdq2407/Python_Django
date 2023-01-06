from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    # rs = HttpResponse()
    # rs.writelines("<h1>xin chao</h1>")
    # rs.write("day la home")
    # return rs
    return render(req,'pages/home.html')
def contact(req):
    return render(req, 'pages/contact.html')

