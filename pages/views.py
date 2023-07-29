from django.shortcuts import render
from django.http import HttpResponse

def homeview(*args,**kwargs):
    return HttpResponse("<center><ul><h1>Home page</h1></ul></center>\n <h1>To register pls enter /accounts/signup</h1>\n<h1>To login pls enter /user_auth</h1>\n <h1>To access polls pls enter /polls</h1>\n <h1>To access webapp pls enter /webapp</h1>\n <h1>To access webapp2 pls enter /webapp2</h1>\n <h1>To access blog pls enter /blog</h1>")
# Create your views here.
