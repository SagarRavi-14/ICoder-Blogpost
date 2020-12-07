from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Contact
from blog.models import Post
from django.contrib import messages
# Create your views here.
def home(request):
    allpost = Post.objects.all()
    param = allpost
    
    return render(request,'home/home.html',{'param':param})
    

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        query = request.POST.get('query',"")
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(query)<4:
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name=name,email=email,phone=phone,query=query)
            contact.save()
            messages.success(request,"Your message has been sent")

    return render(request,'home/contact.html')

def search(request):
    search = request.GET.get('search')
    allpostsTitle = Post.objects.filter(title__icontains=search)
    allpostsContent = Post.objects.filter(content__icontains=search)
    allpostsAuthor = Post.objects.filter(author__icontains=search)
    allposts=allpostsTitle.union(allpostsContent.union(allpostsAuthor))
   
    if len(allposts)<1:
         messages.error(request,f'Search results for {search} not found' )
    else:
         
         messages.success(request,f'Search results for {search}')
    param = {'allposts':allposts,'query':search}
    return render(request,'home/search.html',param)

def handleSignup(request):
    if request.method=='POST':
        username = request.POST['name']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(username)>15:
            messages.error(request,'Username Must be of 15 character')
            return redirect("home")
        if password1!=password2:
            messages.error(request,'Password not matched')
            return redirect("home")
        if not username.isalnum():
            messages.error(request,"Username only contain alphabet and numbers")
            return redirect("home")

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'your account has been created')
        return redirect('home')

    else:
        return HttpResponse("404 not found")


def handleLogin(request):
    if request.method=="POST":
        loginname = request.POST['login-name']
        lpassword = request.POST['lpassword']
        user = authenticate(username=loginname , password=lpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"You are logged in successfully")
            return redirect('home')
        else:
            messages.error(request,'Sorry crediential not match ,please try again!!!')
            return redirect('home')
    else:
        return HttpResponse("404 not found")

def handleLogout(request):
    logout(request)
    messages.success(request,'You are logged out successfully')
    return redirect('home')