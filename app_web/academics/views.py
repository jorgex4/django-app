from django.shortcuts import render
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
        else:
            form = Userform()
           # return.redirect('list')
    return render(request,'academics/create_user.html',{'forms':form}) 
    #return HttpResponse(" Creater a new user")

