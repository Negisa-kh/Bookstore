from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login as auth_login
import random

# Create your views here.
def signup(request):
    message = ""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.get(number=form.cleaned_data.get("number"))
            if user != None:
                form.add_error("number", ValueError("number already exist"))
                
            else:
                if form.cleaned_data.get("code") == 0:
                    code = random.randint(100000, 999999)
                    print("code: ", code)
                    request.session["code"] = code
                    # send code to number
                    message = "code sent"
                else:
                    if code == request.sesison.get("code"):
                        user = User()
                        user.fill(form)
                        user.name = form.cleaned_data.get("name")
                        user.password = make_password(form.cleaned_data.get("password"))
                        user.number = form.cleaned_data.get("number")
                        User.objects.create(user)
                        next = request.POST.get("next")
                        return redirect(next)
                    else:
                        message = "invalid code"

    else:
        form = SignupForm()
    
    return render(request, "users/signup.html", {"form": form, "message":message})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(number=form.cleaned_data.get("number"))
            if user != None:
                if form.cleaned_data.get("login_mode") == "password":
                        if user.password == form.cleaned_data.get("password"):
                            auth_login(request, user)
                            return redirect(request.POST.get("next"))

                        else:
                            message = "invalid number or password"
                            
                else:
                    if form.cleaned_data.get("code") == 0:
                        code = random.randint(100000, 999999)
                        print("code: ", code)
                        request.session["code"] = code
                        # send code to number
                        message = "code sent"
                    else:
                        if code == request.sesison.get("code"):

                            auth_login(request, user)
                            return redirect(request.POST.get("next"))
            else:
                form.add_error("number", "number not exist")
    else:
        form = LoginForm()
    return render(request, "users/log_in.html", {"form":form, "message":message})