from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Product
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages


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
                messages.success(request,"注册成功")
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
            messages.success(request,"登录成功")
            return redirect('index:index')


def logout(request):
    if request.method == 'POST':
        user = auth.logout(request)
        return redirect('index:index')


@login_required  # 仅当用户登录了才能跳转到此页面，哪怕直接输入/user/publish
def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    elif request.method == 'POST':
        title = request.POST['shoes_title']
        intro = request.POST['shoes_introduce']
        try:    # 用户未上传图片，会报错
            icon = request.FILES['shoes_small_picture']
            image = request.FILES['shoes_big_picture']

            # 将上述用户提交的信息存放到数据库
            product = Product()
            product.title = title
            product.intro = intro
            product.icon = icon
            product.image = image
            product.pub_date = timezone.datetime.now()  # 记录用户点击发布按钮时的时间
            product.publish_user = request.user

            product.save()

            return redirect('index:index')
            
        except Exception as err:
            return render(request,'publish.html',{'picture_error':'请上传图片'})


def publish_list(request):
    products = Product.objects
    return render(request, 'publish_list.html',{'products':products})


def publish_list_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id) # 主键形式获取Product表中的对应ID
    return render(request, 'publish_list_detail.html',{'product':product})