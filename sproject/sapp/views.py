from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    user = User.objects.last()
    print(user.email)
    return HttpResponse("Home Page..")


def signup(request):
    if request.method == "POST":
        fm = UserCreationForm()
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        alluser = User.objects.all()
        for users in alluser:
            if users.username == username:
                return render(request, "signup.html", {"error": "your username already register try something new.", "form": fm})
            else:
                continue
        fm = User.objects.create_user(username, pass1, pass2)
        fm.save()
        return HttpResponse("account created ")
    else:
        fm = UserCreationForm()

        return render(request, "signup.html", {"form": fm})


def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/profile')
        return HttpResponse("user is none")
    else:
        fm = AuthenticationForm()
        return render(request, "login.html", {"form": fm})


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", {"username": request.user})
    else:
        return HttpResponseRedirect("/login")


def logoutt(request):
    logout(request)
    return HttpResponseRedirect("/login")
