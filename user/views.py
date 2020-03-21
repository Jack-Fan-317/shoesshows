from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        user_name = request.POST['username']
        password1 = request.POST['password_initial']
        password2 = request.POST['password_confirm']
        try:
            User.objects.get(username=user_name)
            # 若用户名已存在,返回用户名已存在提示
            return render(request, 'signup.html', {'username_error':'该用户名已存在'})
        except User.DoesNotExist:
            # 若用户名不存在,判断密码是否有误
            if password1 == password2:
                User.objects.create_user(username=user_name, password=password1)
                # 重定向到另一个页面
                return redirect('index:index')
            else:
                return render(request, 'signup.html', {'password_error':'您输入的密码不一致'})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        user = auth.authenticate(username=user_name,password=pass_word)
        if user is None:
            return render(request, 'login.html', {'error':'您输入的用户名或密码不正确'})
        else:
            auth.login(request, user)
            return redirect('index:index')


def logout(request):
    if request.method == 'POST':
        user = auth.logout(request)
        return redirect('index:index')