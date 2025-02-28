from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages
from .models import Post
# from .models import Blog
def home(request):
    return render(request,'index.html')
def login(request):
    # return render(request,'login.html')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        x=authenticate(username=username,password=password)
        if x is not None:
            auth_login(request,x)
            return redirect('project')
        else:
            messages.error(request, 'Please enter details')
    else:
        return render(request,'login.html')
def register(request):
    # return render(request,'register.html')
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if email and username and password1 and password2:
                c=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password1,username=username)
                c.save()
                return redirect("login")
        else:
            messages.error(request, 'Please fill in all required fields')
    else:
        return render(request,"register.html")
def project(request):
    return render(request,'project.html')
def profile(request):
    return render(request,'profile.html')
def index(request):
    return render(request,'index.html')
def blog(request):
    return render(request,'blog.html')
def saved(request):
    post=Post.objects.all()
    return render(request,"saved.html",{'post':post})
def Blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author_name = request.POST.get('author_name')
        new_entry = Post(title=title, content=content, author_name=author_name)
        new_entry.save()
        return redirect('saved')
    else:
        return render(request,"blog.htmlx")
    