from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    return HttpResponse(" ::Welcome to my site  ::")

def list_users(request):
    users = User.objects.all()
    return render(request,'academics/list_user.html',{'users':users})
    #return HttpResponse(" here you find a list of users")

def create_user(request):
    return HttpResponse(" Creater a new user")

