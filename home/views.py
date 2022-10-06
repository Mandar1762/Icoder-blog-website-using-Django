from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# from .models import Post

# Create your views here.


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        if len(name) < 2 or len(email) < 9 or len(phone) < 10 or len(desc) < 4:
            messages.warning(request, "please fill form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc)
            contact.save()
            messages.success(request, 'Query has been successfully sent')
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def handleSignUp(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for erroneous input
        if len(username) < 5:
            messages.error(request, "Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "User name should contain only letters and numbers ")
            return redirect('home')

        if (pass1 != pass2):
            messages.error(request, "Passwords do not match")
            return redirect('home')

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your iCoder account has been Sucessfully created ")
        return redirect('home')

    else:
        return HttpResponse("404 - not found")


# def search(request):
#  query = request.GET['query']
#  allposts = Post.objects.filter(title__icontains=query)
##return render(request, 'home/search.html', params)

def handleLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In ")
            return redirect('home')

        else:
            messages.error(request, "invalid Credentials please try again!")
            return redirect('home')


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')



