from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .form import LoginForm
from .models import User


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.password == password:
                    r = redirect("home/")
                    r.set_signed_cookie('username', username, salt="MyDj")
                    return r
                else:
                    form.add_error('password', '密码错误')
            except User.DoesNotExist:
                form.add_error('username', '用户不存在')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    form = LoginForm()
    cookies_exist = request.COOKIES.get("username", '')
    if cookies_exist:
        try:
            request.get_signed_cookie('username', salt='MyDj')
        except:
            return render(request, "login.html", {'form': form})
        return render(request, "home.html")
    else:
        return render(request, "login.html", {'form': form})


def upload(request):
    if request.method == "GET":
        return render(request, "uploadFile.html")


def logout(request):
    response = redirect("/login/")
    keys = request.COOKIES.keys()
    for one in keys:
        response.delete_cookie(one)
        del request.session['username']
    return response
