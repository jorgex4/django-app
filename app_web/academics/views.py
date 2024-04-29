from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import Userform

# Create your views here.
def index(request):
    return HttpResponse(" ::Welcome to my site  ::")

def list_users(request):
    users = User.objects.all()
    return render(request,'academics/list_user.html',{'users':users})
    #return HttpResponse(" here you find a list of users")

def create_user(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = Userform()
           # return.redirect('list')
    return render(request,'academics/create_user.html',{'form':form}) 
    #return HttpResponse(" Creater a new user")

