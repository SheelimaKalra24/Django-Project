from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import posts
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout


# Create your views here.
def login_view(req):
    if req.method == 'POST':
        userName = req.POST.get('userName')
        password1 = req.POST.get('password')
        user = authenticate(req, username = userName,password=password1)
        if user is not None:
            login(req,user)
            return redirect('home')
        else:
            messages.error(req,"Invalid username or password")
    return render(req, 'login.html')

def logout_view(req):
    if req.method == 'POST':
        logout(req)
        messages.info(req, "You have been logged out successfully.")
        return redirect('login') 
    return render(req, 'logout.html')

def createUser(req):
    if req.method == 'POST':
        firstName = req.POST.get('firstName')
        lastName = req.POST.get('lastName')
        userName = req.POST.get('userName')
        password1 = req.POST.get('password1')
        password2 = req.POST.get('password2')
        user = User.objects.filter( username = userName)
        if password1 == password2:
            if user.exists():
                messages.info(req, "user already exist")
            else:
                user = User(  username = userName, first_name = firstName, last_name = lastName)
                user.set_password(password1)
                user.save()
                messages.info(req, "user created succesfully") 
    return render(req, 'register.html')


def home(req):
    post = posts.objects.all()
    if req.method == 'POST':
        image = req.FILES.get('image')
        title = req.POST.get('title')
        des = req.POST.get('des')

        post = posts(title = title, des= des, image = image)
        post.save()
        return HttpResponse("data added successfully")
    return render(req, 'index.html', {"posts": post})

def update(req, id):
    post = posts.objects.all()
    updatePost = get_object_or_404(posts, id = id)
    if req.method == 'POST':
        updatePost.image = req.FILES.get('image')
        updatePost.title = req.POST.get('title')
        updatePost.des = req.POST.get('des')
        updatePost.save()
        return HttpResponse("update post")
    return render(req, 'index.html' , {"posts": post, "update": updatePost})

def DeletePost(req, id):
    post = get_object_or_404(posts , id=id)
    post.delete()
    return HttpResponse("the post deleted successfully")

def post_detail(request, post_id):
    post = get_object_or_404(posts, id=post_id)
    return render(request, 'postdetail.html', {'post': post})
