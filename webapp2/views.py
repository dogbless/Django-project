from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
@login_required(login_url="/user_auth/") 
def index1(request):
    return render(request,"index1.html")





# Create your views here.
